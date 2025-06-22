"""
Integration module for chest and shop randomization
This module handles the integration of chest and shop randomization
with shared logic to maintain game progression
"""

import random
from terranigma_randomizer.constants.items import (
    ITEM_DATABASE, PROGRESSION_KEY_ITEMS, ITEM_NAME_TO_ID, 
    ItemTypes, get_item_name, get_item_info, PORTRAIT_CHEST_ID, PORTRAIT_ITEM_ID
)
from terranigma_randomizer.constants.chests import CHEST_MAP, KNOWN_CHESTS
from terranigma_randomizer.constants.shops import (
    KNOWN_SHOPS, SHOP_ID_TO_INDEX, decimal_to_bcd, bcd_to_decimal
)
from terranigma_randomizer.constants.progression import (
    get_accessible_areas, get_accessible_chests, get_progression_tier,
    GAME_AREAS, PROGRESSION_AREAS
)
from terranigma_randomizer.utils.logic import (
    create_seeded_rng, shuffle_array, validate_game_progress, get_chest_location_name
)
from terranigma_randomizer.randomizers.chest import (
    read_chests_from_rom, write_chests_to_rom
)
from terranigma_randomizer.randomizers.shop import (
    read_shops_from_rom, write_shops_to_rom, 
    calculate_item_price, determine_item_limit,
    validate_shop_prices, validate_shop_item_counts
)

def preserve_key_items_across_evolution(shop_contents):
    """
    Ensure that key items placed in any shop of an evolution group
    appear in ALL stages of that shop. This prevents key items from
    becoming inaccessible due to town development.
    
    Args:
        shop_contents (dict): Map of shop IDs to items
        
    Returns:
        dict: Adjusted shop contents with key items preserved
    """
    print("Preserving key items across shop evolution stages...")
    
    # Evolution groups that need key item preservation
    evolution_groups = {
        'LUMINA': [2, 3],
        'SANCTUAR': [5, 6], 
        'LOIRE': [13, 14, 17, 19],
        'FREEDOM_INN': [18, 21, 22],
        'FREEDOM_MAIN': [24, 25, 27, 28],
        'LITZ': [30, 32],
        'SUNCOAST': [36, 37, 38, 39],
        'NIRLAKE': [15, 16, 42]
    }
    
    # For each evolution group, collect all key items and ensure they appear in all stages
    for group_name, shop_ids in evolution_groups.items():
        # Collect all key items from all shops in this group
        group_key_items = []
        shops_with_content = []
        
        for shop_id in shop_ids:
            if shop_id in shop_contents:
                shops_with_content.append(shop_id)
                # Find key items in this shop
                for item in shop_contents[shop_id]:
                    if item.get('name') in PROGRESSION_KEY_ITEMS:
                        # Check if this key item is already in our list
                        already_added = any(ki['name'] == item['name'] for ki in group_key_items)
                        if not already_added:
                            group_key_items.append(item.copy())
        
        if group_key_items and shops_with_content:
            print(f"Evolution group {group_name} has {len(group_key_items)} key items to preserve across {len(shops_with_content)} shops")
            for item in group_key_items:
                print(f"  - {item['name']}")
            
            # Ensure each shop in the group has all the key items
            for shop_id in shops_with_content:
                if shop_id not in shop_contents:
                    shop_contents[shop_id] = []
                
                # Get current non-key items in this shop
                non_key_items = [item for item in shop_contents[shop_id] 
                                if item.get('name') not in PROGRESSION_KEY_ITEMS]
                
                # Rebuild shop inventory: key items first, then non-key items
                shop_contents[shop_id] = []
                
                # Add all key items from the group
                for key_item in group_key_items:
                    shop_contents[shop_id].append(key_item.copy())
                
                # Add back non-key items up to shop capacity
                shop_index = SHOP_ID_TO_INDEX.get(shop_id)
                if shop_index is not None:
                    original_shop = KNOWN_SHOPS[shop_index]
                    max_items = len(original_shop['items'])
                    
                    # Calculate how many non-key items we can fit
                    remaining_slots = max_items - len(group_key_items)
                    if remaining_slots > 0:
                        # Add as many non-key items as will fit
                        items_to_add = min(len(non_key_items), remaining_slots)
                        shop_contents[shop_id].extend(non_key_items[:items_to_add])
                
                print(f"  Shop {shop_id} now has {len(shop_contents[shop_id])} items ({len(group_key_items)} key items)")
    
    return shop_contents

def handle_shared_offset_shops(shop_contents):
    """
    Handle shops that share the same file offset but are NOT in the same evolution group.
    For evolution groups, we use preserve_key_items_across_evolution instead.
    
    This specifically handles:
    - Shop 18 (Freedom Inn) sharing offset with shops 37/38 (Suncoast)
    
    Args:
        shop_contents (dict): Map of shop IDs to items
        
    Returns:
        dict: Adjusted shop contents
    """
    print("Handling shared offset shops (non-evolution)...")
    
    # Define which shops share offsets but are NOT evolution groups
    SHARED_OFFSET_CONFLICTS = {
        0x19D2A2: {
            'shops': {
                18: 'FREEDOM_INN',
                37: 'SUNCOAST', 
                38: 'SUNCOAST'
            },
            'primary': 38  # Shop 38 wins (written last)
        }
    }
    
    for offset, conflict_info in SHARED_OFFSET_CONFLICTS.items():
        shops_at_offset = conflict_info['shops']
        primary_shop = conflict_info['primary']
        
        # Check if any non-primary shops have key items
        key_items_to_preserve = []
        
        for shop_id, group in shops_at_offset.items():
            if shop_id == primary_shop or shop_id not in shop_contents:
                continue
            
            # Find key items in this shop
            shop_key_items = [item for item in shop_contents[shop_id] 
                             if item.get('name') in PROGRESSION_KEY_ITEMS]
            
            if shop_key_items:
                print(f"Shop {shop_id} ({group}) has {len(shop_key_items)} key items at shared offset {hex(offset)}")
                for item in shop_key_items:
                    print(f"  - {item['name']}")
                    key_items_to_preserve.extend(shop_key_items)
                
                # Remove key items from the non-primary shop
                shop_contents[shop_id] = [item for item in shop_contents[shop_id] 
                                         if item.get('name') not in PROGRESSION_KEY_ITEMS]
        
        # Add preserved key items to the primary shop
        if key_items_to_preserve and primary_shop in shop_contents:
            print(f"Moving {len(key_items_to_preserve)} key items to primary shop {primary_shop}")
            # Add key items at the beginning of the shop
            shop_contents[primary_shop] = key_items_to_preserve + shop_contents[primary_shop]
            
            # Trim if necessary to fit shop capacity
            shop_index = SHOP_ID_TO_INDEX.get(primary_shop)
            if shop_index is not None:
                original_shop = KNOWN_SHOPS[shop_index]
                max_items = len(original_shop['items'])
                if len(shop_contents[primary_shop]) > max_items:
                    print(f"Trimming shop {primary_shop} from {len(shop_contents[primary_shop])} to {max_items} items")
                    shop_contents[primary_shop] = shop_contents[primary_shop][:max_items]
    
    return shop_contents

def get_evolution_group(shop_id):
    """Get the evolution group for a shop ID"""
    # Inline shop evolution groups data
    SHOP_EVOLUTION_GROUPS = {
        'LUMINA': [
            {'id': 2, 'stage': 1, 'location': 'Lumina (stage 1)', 'fileOffset': 0x19D077},
            {'id': 3, 'stage': 2, 'location': 'Lumina (stage 2/3)', 'fileOffset': 0x19D084}
        ],
        'SANCTUAR': [
            {'id': 6, 'stage': 1, 'location': 'Sanctuar (pre-birds)', 'fileOffset': 0x19D0AE},
            {'id': 5, 'stage': 2, 'location': 'Sanctuar (birds)', 'fileOffset': 0x19D09D}
        ],
        'LOIRE': [
            {'id': 13, 'stage': 1, 'location': 'Loire - Shop', 'fileOffset': 0x19D125},
            {'id': 14, 'stage': 2, 'location': 'Loire - Shop Weapons', 'fileOffset': 0x19D136},
            {'id': 17, 'stage': 3, 'location': 'Loire - Merchant', 'fileOffset': 0x19D175},
            {'id': 19, 'stage': 3, 'location': 'Loire - Merchant', 'fileOffset': 0x19D182}
        ],
        'FREEDOM_INN': [
            {'id': 18, 'stage': 1, 'location': 'Freedom - Inn - Merchant', 'fileOffset': 0x19D2A2},
            {'id': 21, 'stage': 2, 'location': 'Freedom - Inn - Merchant', 'fileOffset': 0x19D19C},
            {'id': 22, 'stage': 2, 'location': 'Freedom - Inn - Merchant', 'fileOffset': 0x19D1B1}
        ],
        'FREEDOM_MAIN': [
            {'id': 24, 'stage': 2, 'location': 'Freedom - Weapons', 'fileOffset': 0x19D1CA},
            {'id': 25, 'stage': 2, 'location': 'Freedom - Armor (Stage 2)', 'fileOffset': 0x19D1D7},
            {'id': 27, 'stage': 3, 'location': 'Freedom - Weapons (Stage 3)', 'fileOffset': 0x19D1E4},
            {'id': 28, 'stage': 3, 'location': 'Freedom - Armor', 'fileOffset': 0x19D1F5}
        ],
        'LITZ': [
            {'id': 30, 'stage': 1, 'location': 'Litz - Merchant', 'fileOffset': 0x19D206},
            {'id': 32, 'stage': 2, 'location': 'Litz - Merchant (Stage Final)', 'fileOffset': 0x19D217}
        ],
        'SUNCOAST': [
            {'id': 36, 'stage': 1, 'location': 'Suncoast- Left Merchant', 'fileOffset': 0x19D26F},
            {'id': 37, 'stage': 1, 'location': 'Suncoast- Right Merchant', 'fileOffset': 0x19D2A2},
            {'id': 38, 'stage': 2, 'location': 'Suncoast Merchant', 'fileOffset': 0x19D2A2},
            {'id': 39, 'stage': 2, 'location': 'Suncoast - Merchant', 'fileOffset': 0x19D278}
        ],
        'NIRLAKE': [
            {'id': 15, 'stage': 1, 'location': 'Nirlake - House', 'fileOffset': 0x19D147},
            {'id': 16, 'stage': 2, 'location': '1st Ave. - Merchant', 'fileOffset': 0x19D15C},
            {'id': 42, 'stage': 3, 'location': 'Nirlake - Hotel - Room 2', 'fileOffset': 0x19D262}
        ]
    }
    
    for group_name, shops in SHOP_EVOLUTION_GROUPS.items():
        for shop in shops:
            if shop['id'] == shop_id:
                return group_name, shop['stage']
    return None, None

def get_shops_at_same_location(shop_id):
    """Get all shop IDs that share the same physical location"""
    # Inline shop evolution groups data
    SHOP_EVOLUTION_GROUPS = {
        'LUMINA': [
            {'id': 2, 'stage': 1, 'location': 'Lumina (stage 1)', 'fileOffset': 0x19D077},
            {'id': 3, 'stage': 2, 'location': 'Lumina (stage 2/3)', 'fileOffset': 0x19D084}
        ],
        'SANCTUAR': [
            {'id': 6, 'stage': 1, 'location': 'Sanctuar (pre-birds)', 'fileOffset': 0x19D0AE},
            {'id': 5, 'stage': 2, 'location': 'Sanctuar (birds)', 'fileOffset': 0x19D09D}
        ],
        'LOIRE': [
            {'id': 13, 'stage': 1, 'location': 'Loire - Shop', 'fileOffset': 0x19D125},
            {'id': 14, 'stage': 2, 'location': 'Loire - Shop Weapons', 'fileOffset': 0x19D136},
            {'id': 17, 'stage': 3, 'location': 'Loire - Merchant', 'fileOffset': 0x19D175},
            {'id': 19, 'stage': 3, 'location': 'Loire - Merchant', 'fileOffset': 0x19D182}
        ],
        'FREEDOM_INN': [
            {'id': 18, 'stage': 1, 'location': 'Freedom - Inn - Merchant', 'fileOffset': 0x19D2A2},
            {'id': 21, 'stage': 2, 'location': 'Freedom - Inn - Merchant', 'fileOffset': 0x19D19C},
            {'id': 22, 'stage': 2, 'location': 'Freedom - Inn - Merchant', 'fileOffset': 0x19D1B1}
        ],
        'FREEDOM_MAIN': [
            {'id': 24, 'stage': 2, 'location': 'Freedom - Weapons', 'fileOffset': 0x19D1CA},
            {'id': 25, 'stage': 2, 'location': 'Freedom - Armor (Stage 2)', 'fileOffset': 0x19D1D7},
            {'id': 27, 'stage': 3, 'location': 'Freedom - Weapons (Stage 3)', 'fileOffset': 0x19D1E4},
            {'id': 28, 'stage': 3, 'location': 'Freedom - Armor', 'fileOffset': 0x19D1F5}
        ],
        'LITZ': [
            {'id': 30, 'stage': 1, 'location': 'Litz - Merchant', 'fileOffset': 0x19D206},
            {'id': 32, 'stage': 2, 'location': 'Litz - Merchant (Stage Final)', 'fileOffset': 0x19D217}
        ],
        'SUNCOAST': [
            {'id': 36, 'stage': 1, 'location': 'Suncoast- Left Merchant', 'fileOffset': 0x19D26F},
            {'id': 37, 'stage': 1, 'location': 'Suncoast- Right Merchant', 'fileOffset': 0x19D2A2},
            {'id': 38, 'stage': 2, 'location': 'Suncoast Merchant', 'fileOffset': 0x19D2A2},
            {'id': 39, 'stage': 2, 'location': 'Suncoast - Merchant', 'fileOffset': 0x19D278}
        ],
        'NIRLAKE': [
            {'id': 15, 'stage': 1, 'location': 'Nirlake - House', 'fileOffset': 0x19D147},
            {'id': 16, 'stage': 2, 'location': '1st Ave. - Merchant', 'fileOffset': 0x19D15C},
            {'id': 42, 'stage': 3, 'location': 'Nirlake - Hotel - Room 2', 'fileOffset': 0x19D262}
        ]
    }
    
    for group_name, shops in SHOP_EVOLUTION_GROUPS.items():
        for shop in shops:
            if shop['id'] == shop_id:
                return [shop['id'] for shop in shops]
    return [shop_id]

# Helper function to get the max shop items
def get_max_shop_items(shop_id, options):
    """
    Get the maximum number of items a shop can hold
    
    Args:
        shop_id: Shop ID (can be string or int)
        options (dict): Randomization options
        
    Returns:
        int: Maximum number of items for the shop
    """
    # Convert shop_id to int if it's a string
    if isinstance(shop_id, str) and shop_id.isdigit():
        shop_id = int(shop_id)
    elif isinstance(shop_id, str):
        # If it's a non-numeric string, try to extract number
        try:
            shop_id = int(''.join(filter(str.isdigit, shop_id)))
        except:
            return 5  # Default
        
    shop_index = SHOP_ID_TO_INDEX.get(shop_id)
    if shop_index is not None:
        original_shop = KNOWN_SHOPS[shop_index]
        original_count = len(original_shop['items'])
        
        # If user wants more items, allow more than original
        items_per_shop = options.get('items_per_shop', 'normal')
        if items_per_shop == 'more':
            return min(15, original_count + 4)  # Add up to 4 more items, max 15
        elif items_per_shop == 'fewer':
            return max(2, original_count - 2)  # Remove up to 2 items, min 2
        else:
            return original_count
    
    # Default based on option
    items_per_shop = options.get('items_per_shop', 'normal')
    if items_per_shop == 'more':
        return 8
    elif items_per_shop == 'fewer':
        return 3
    else:
        return 5

def create_enhanced_logical_placement(verbose=False, options=None):
    """
    Enhanced logical placement function that incorporates shops into progression logic
    IMPORTANT: Protects Portrait chest (chest 150) from randomization
    
    Args:
        verbose (bool): Whether to print detailed logs
        options (dict): Randomization options
        
    Returns:
        dict: Map of chest IDs to item IDs and shop placements or None if failed
    """
    if options is None:
        options = {}
    
    # Set a higher recursion limit to handle complex logic
    import sys
    sys.setrecursionlimit(10000)
    
    if verbose:
        print("Creating logical placement with shop integration...")
        print(f"NOTE: Portrait chest ({PORTRAIT_CHEST_ID}) will remain in vanilla location")
    
    # Prepare our chest and shop placement maps
    chest_contents = {}
    shop_contents = {}
    used_chests = set()
    
    # CRITICAL: Immediately protect the Portrait chest
    chest_contents[PORTRAIT_CHEST_ID] = PORTRAIT_ITEM_ID
    used_chests.add(PORTRAIT_CHEST_ID)
    
    if verbose:
        print(f"Protected Portrait chest {PORTRAIT_CHEST_ID} with item {PORTRAIT_ITEM_ID}")
    
    # Track placed items to ensure only one copy of each in the world
    placed_items = set()
    key_items_placed = set()
    
    # Portrait item is now considered "placed"
    placed_items.add(PORTRAIT_ITEM_ID)
    
    # Track Starstone placements explicitly
    starstone_locations = []
    
    # Track how many items we've allocated to each shop
    shop_item_counts = {}
    
    # Define shops that should NOT get key items due to offset conflicts
    UNSAFE_SHOPS_FOR_KEY_ITEMS = [18, 37]  # Both share offset 0x19D2A2
    
    # Decide where each key item will be placed - chest or shop
    key_item_placements = {}
    for key_item in PROGRESSION_KEY_ITEMS:
        # 30% chance for key item to be in a shop instead of a chest
        key_item_placements[key_item] = 'shop' if random.random() < 0.3 else 'chest'
    
    # Always place Giant Leaves in a chest for guaranteed early access
    key_item_placements['Giant Leaves'] = 'chest'
    
    if verbose:
        print("Key item placement decisions:")
        for item, placement in key_item_placements.items():
            print(f"- {item}: {placement}")
    
    # Place Giant Leaves in Tree Cave
    giant_leaves_id = ITEM_NAME_TO_ID.get('Giant Leaves')
    early_accessible_chests = [
        chest_id for chest_id in PROGRESSION_AREAS['TREE_CAVE_ENTRANCE']['contains']
        if chest_id not in used_chests  # Exclude Portrait chest
    ]
    
    if giant_leaves_id and early_accessible_chests:
        shuffle_array(early_accessible_chests)
        chosen_chest_id = early_accessible_chests[0]
        
        chest_contents[chosen_chest_id] = giant_leaves_id
        used_chests.add(chosen_chest_id)
        key_items_placed.add('Giant Leaves')
        placed_items.add(giant_leaves_id)
        
        if verbose:
            print(f"Placed Giant Leaves in chest {chosen_chest_id}")
    else:
        if verbose:
            print("Failed to place Giant Leaves - no suitable chests")
        return None
    
    # Create collections of early, mid, and late game shops
    early_shops = [shop for shop in KNOWN_SHOPS if get_progression_tier(shop['location']) == 0]
    mid_shops = [shop for shop in KNOWN_SHOPS 
                if get_progression_tier(shop['location']) == 1 or 
                   get_progression_tier(shop['location']) == 2]
    late_shops = [shop for shop in KNOWN_SHOPS 
                 if get_progression_tier(shop['location']) == 3 or 
                    get_progression_tier(shop['location']) == 4]
    
    # We'll now simulate collecting items and use that to determine where to place each item
    # Start with Giant Leaves collected
    collected_items = {'Giant Leaves'}
    
    # Helper function to place an item in a shop
    def place_item_in_shop(item_name, shop_tiers, base_price):
        item_id = ITEM_NAME_TO_ID.get(item_name)
        if not item_id:
            if verbose:
                print(f"Missing ID for item: {item_name}")
            return False
        
        # Don't place if the item is already placed somewhere
        if item_id in placed_items:
            if verbose:
                print(f"Item {item_name} is already placed elsewhere")
            return False
        
        # Choose an available shop with space
        if not shop_tiers:
            if verbose:
                print(f"No shops available for {item_name}")
            return False
        
        # Sort shops by available space, but exclude unsafe shops for key items
        available_shops = []
        for shop in shop_tiers:
            shop_id = shop['id']
            
            # CRITICAL: Skip unsafe shops for key items
            if shop_id in UNSAFE_SHOPS_FOR_KEY_ITEMS and item_name in PROGRESSION_KEY_ITEMS:
                if verbose:
                    print(f"Skipping shop {shop_id} for key item {item_name} due to offset conflict")
                continue
            
            current_count = shop_item_counts.get(shop_id, 0)
            max_items = get_max_shop_items(shop_id, options)
            
            # Skip if shop is full
            if current_count >= max_items:
                continue
                
            available_shops.append(shop)
            
        if not available_shops:
            if verbose:
                print(f"No shops with available space for {item_name}")
            return False
            
        shuffle_array(available_shops)
        chosen_shop = available_shops[0]
        shop_id = chosen_shop['id']
        
        if shop_id not in shop_contents:
            shop_contents[shop_id] = []
            shop_item_counts[shop_id] = 0
        
        # Add variation to price
        price = base_price + random.randint(0, base_price // 2)
        
        # Get item type from database
        item_hex = f"{item_id:04X}"
        item_type = ITEM_DATABASE.get(item_hex, {}).get('type', ItemTypes.KEY_ITEM)
        
        shop_contents[shop_id].append({
            'itemId': item_id,
            'name': item_name,
            'type': item_type,
            'price': price,
            'bcdPrice': decimal_to_bcd(price),
            'limit': 1  # Limit all unique items to 1 purchase
        })
        
        # Update shop item count
        shop_item_counts[shop_id] = shop_item_counts.get(shop_id, 0) + 1
        
        key_items_placed.add(item_name)
        collected_items.add(item_name)
        placed_items.add(item_id)
        
        if verbose:
            print(f"Placed {item_name} in shop {shop_id} ({chosen_shop['location']}) for {price} gems")
        return True
    
    # Helper function to place an item in a chest
    def place_item_in_chest(item_name, accessible_chests):
        item_id = ITEM_NAME_TO_ID.get(item_name)
        if not item_id:
            if verbose:
                print(f"Missing ID for item: {item_name}")
            return False
        
        # Don't place if the item is already placed somewhere
        if item_id in placed_items:
            if verbose:
                print(f"Item {item_name} is already placed elsewhere")
            return False
        
        # Filter out already used chests (including Portrait chest)
        available_chests = [chest_id for chest_id in accessible_chests if chest_id not in used_chests]
        
        if not available_chests:
            if verbose:
                print(f"No chests available for {item_name}")
            return False
        
        shuffle_array(available_chests)
        chosen_chest_id = available_chests[0]
        
        chest_contents[chosen_chest_id] = item_id
        used_chests.add(chosen_chest_id)
        key_items_placed.add(item_name)
        collected_items.add(item_name)
        placed_items.add(item_id)
        
        if verbose:
            print(f"Placed {item_name} in chest {chosen_chest_id}")
        return True
    
    # Place key progression items in a specific order to maintain game logic
    
    # 1. Place Ra Dewdrop - needed for Ra Tree Boss
    if key_item_placements['Ra Dewdrop'] == 'shop' and early_shops:
        if not place_item_in_shop('Ra Dewdrop', early_shops, 120):
            # Fallback to chest placement
            early_chests_for_ra_dewdrop = [
                chest_id for chest_id in PROGRESSION_AREAS['UNDERWORLD_START']['contains'] 
                if chest_id not in used_chests
            ] + [
                chest_id for chest_id in PROGRESSION_AREAS['TREE_CAVE_ENTRANCE']['contains'] 
                if chest_id not in used_chests
            ]
            
            if not place_item_in_chest('Ra Dewdrop', early_chests_for_ra_dewdrop):
                if verbose:
                    print("Failed to place Ra Dewdrop")
                return None
    else:
        # Place in chest
        early_chests_for_ra_dewdrop = [
            chest_id for chest_id in PROGRESSION_AREAS['UNDERWORLD_START']['contains'] 
            if chest_id not in used_chests
        ] + [
            chest_id for chest_id in PROGRESSION_AREAS['TREE_CAVE_ENTRANCE']['contains'] 
            if chest_id not in used_chests
        ]
        
        if not place_item_in_chest('Ra Dewdrop', early_chests_for_ra_dewdrop):
            if verbose:
                print("Failed to place Ra Dewdrop")
            return None
    
    # 2. Place RocSpear - needed for Grecliff advanced areas
    remaining_early_chests = [
        chest_id for chest_id in early_accessible_chests 
        if chest_id not in used_chests
    ]
    
    if key_item_placements['RocSpear'] == 'shop' and early_shops:
        if not place_item_in_shop('RocSpear', early_shops, 180):
            # Fallback to chest placement
            if not place_item_in_chest('RocSpear', remaining_early_chests):
                if verbose:
                    print("Failed to place RocSpear")
                return None
    else:
        # Place in chest
        if not place_item_in_chest('RocSpear', remaining_early_chests):
            if verbose:
                print("Failed to place RocSpear")
            return None
    
    # 3. Place Crystal Thread for ElleCape - needed for Tower 5
    if key_item_placements['Crystal Thread'] == 'shop' and early_shops:
        if not place_item_in_shop('Crystal Thread', early_shops, 250):
            # Fallback to chest placement
            tower_chests = [chest_id for chest_id in PROGRESSION_AREAS['UNDERWORLD_START']['contains'] 
                          if chest_id not in used_chests]
            
            if not place_item_in_chest('Crystal Thread', tower_chests):
                if verbose:
                    print("Failed to place Crystal Thread")
                return None
    else:
        # Place in chest
        tower_chests = [chest_id for chest_id in PROGRESSION_AREAS['UNDERWORLD_START']['contains'] 
                      if chest_id not in used_chests]
        
        if not place_item_in_chest('Crystal Thread', tower_chests):
            if verbose:
                print("Failed to place Crystal Thread")
            return None
    
    # 4. Place Sharp Claws - needed for climbing in Grecliff and beyond
    # Get all areas accessible with current items
    accessible_areas = get_accessible_areas(collected_items)
    accessible_chests = [chest_id for chest_id in get_accessible_chests(collected_items) 
                        if chest_id not in used_chests]
    
    if verbose:
        print(f"Accessible areas with current items: {', '.join(accessible_areas)}")
        print(f"Accessible chests count: {len(accessible_chests)}")
    
    if key_item_placements['Sharp Claws'] == 'shop':
        # Decide if we should place in early shop
        available_shops = early_shops.copy()
        
        if not place_item_in_shop('Sharp Claws', available_shops, 300):
            # Fallback to chest
            if not place_item_in_chest('Sharp Claws', accessible_chests):
                if verbose:
                    print("Failed to place Sharp Claws")
                return None
    else:
        # Place in chest
        if not place_item_in_chest('Sharp Claws', accessible_chests):
            if verbose:
                print("Failed to place Sharp Claws")
            return None
    
    # 5. Place Red Scarf - Needed for Louran
    if key_item_placements['Red Scarf'] == 'shop' and early_shops:
        if not place_item_in_shop('Red Scarf', early_shops, 120):
            # Fallback to chest placement
            mid_chests_for_red_scarf = [
                chest_id for chest_id in PROGRESSION_AREAS['GRECLIFF_BOSS']['contains'] 
                if chest_id not in used_chests
            ] + [
                chest_id for chest_id in PROGRESSION_AREAS['EKLEMATA_REGION']['contains'] 
                if chest_id not in used_chests
            ] + [
                chest_id for chest_id in PROGRESSION_AREAS['LOURAN_REGION']['contains'] 
                if chest_id not in used_chests
            ]
            
            if not place_item_in_chest('Red Scarf', mid_chests_for_red_scarf):
                if verbose:
                    print("Failed to place Red Scarf")
                return None
    else:
        # Place in chest
        mid_chests_for_red_scarf = [
            chest_id for chest_id in PROGRESSION_AREAS['UNDERWORLD_START']['contains'] 
            if chest_id not in used_chests
        ] + [
            chest_id for chest_id in PROGRESSION_AREAS['TREE_CAVE_ENTRANCE']['contains'] 
            if chest_id not in used_chests
        ]
        
        if not place_item_in_chest('Red Scarf', mid_chests_for_red_scarf):
            if verbose:
                print("Failed to place Red Scarf")
            return None
    
    # 6. Place Engagement Ring - needed for Great Lakes Caves
    if key_item_placements['Engagement Ring'] == 'shop' and mid_shops:
        if not place_item_in_shop('Engagement Ring', mid_shops, 120):
            # Fallback to chest placement
            mid_chests_for_engagement_ring = [
                chest_id for chest_id in PROGRESSION_AREAS['GRECLIFF_BOSS']['contains'] 
                if chest_id not in used_chests
            ] + [
                chest_id for chest_id in PROGRESSION_AREAS['EKLEMATA_REGION']['contains'] 
                if chest_id not in used_chests
            ] + [
                chest_id for chest_id in PROGRESSION_AREAS['LOIRE_CASTLE']['contains'] 
                if chest_id not in used_chests
            ] + [
                chest_id for chest_id in PROGRESSION_AREAS['LOURAN_REGION']['contains'] 
                if chest_id not in used_chests
            ] + [
                chest_id for chest_id in PROGRESSION_AREAS['NORFEST_REGION']['contains'] 
                if chest_id not in used_chests
            ]
            
            if not place_item_in_chest('Engagement Ring', mid_chests_for_engagement_ring):
                if verbose:
                    print("Failed to place Engagement Ring")
                return None
    else:
        # Place in chest
        mid_chests_for_engagement_ring = [
            chest_id for chest_id in PROGRESSION_AREAS['UNDERWORLD_START']['contains'] 
            if chest_id not in used_chests
        ] + [
            chest_id for chest_id in PROGRESSION_AREAS['TREE_CAVE_ENTRANCE']['contains'] 
            if chest_id not in used_chests
        ]
        
        if not place_item_in_chest('Engagement Ring', mid_chests_for_engagement_ring):
            if verbose:
                print("Failed to place Engagement Ring")
            return None
    
    # 7. Place Air Herb - needed for Great Lakes Caves
    if key_item_placements['Air Herb'] == 'shop' and mid_shops:
        if not place_item_in_shop('Air Herb', mid_shops, 120):
            # Fallback to chest placement
            mid_chests_for_air_herb = [
                chest_id for chest_id in PROGRESSION_AREAS['GRECLIFF_BOSS']['contains'] 
                if chest_id not in used_chests
            ] + [
                chest_id for chest_id in PROGRESSION_AREAS['EKLEMATA_REGION']['contains'] 
                if chest_id not in used_chests
            ] + [
                chest_id for chest_id in PROGRESSION_AREAS['LOIRE_CASTLE']['contains'] 
                if chest_id not in used_chests
            ] + [
                chest_id for chest_id in PROGRESSION_AREAS['LOURAN_REGION']['contains'] 
                if chest_id not in used_chests
            ] + [
                chest_id for chest_id in PROGRESSION_AREAS['NORFEST_REGION']['contains'] 
                if chest_id not in used_chests
            ]
            
            if not place_item_in_chest('Air Herb', mid_chests_for_air_herb):
                if verbose:
                    print("Failed to place Air Herb")
                return None
    else:
        # Place in chest
        mid_chests_for_air_herb = [
            chest_id for chest_id in PROGRESSION_AREAS['UNDERWORLD_START']['contains'] 
            if chest_id not in used_chests
        ] + [
            chest_id for chest_id in PROGRESSION_AREAS['TREE_CAVE_ENTRANCE']['contains'] 
            if chest_id not in used_chests
        ]
        
        if not place_item_in_chest('Air Herb', mid_chests_for_air_herb):
            if verbose:
                print("Failed to place Air Herb")
            return None

    # Handle Starstones - We need 5 of them to access Astarica
    starstone_id = ITEM_NAME_TO_ID.get('Starstone')
    if not starstone_id:
        if verbose:
            print("Missing ID for Starstone")
        return None

    # Track how many Starstones we've placed
    starstone_count = 0

    # Instead of limiting to specific late areas, use all areas available before Astarica
    # Get all areas that should be accessible before needing Starstones
    pre_astarica_areas = []
    for area_name, area_data in PROGRESSION_AREAS.items():
        # Skip Astarica itself and any areas that require Starstones
        if 'Starstone' in area_data['required'] or 'Starstones5' in area_data['required']:
            continue
        pre_astarica_areas.append(area_name)

    if verbose:
        print(f"Areas available for Starstone placement: {', '.join(pre_astarica_areas)}")

    # Get chests from all areas accessible before Astarica
    available_chests = []
    for area in pre_astarica_areas:
        if area in PROGRESSION_AREAS and 'contains' in PROGRESSION_AREAS[area]:
            for chest_id in PROGRESSION_AREAS[area]['contains']:
                if chest_id not in used_chests and chest_id in CHEST_MAP:  # Only use chests that exist
                    available_chests.append(chest_id)

    # Shuffle the chest list
    shuffle_array(available_chests)

    # Get all shops available before Astarica
    # Shops in pre-Astarica areas - but exclude unsafe shops
    available_shops = []
    for shop in KNOWN_SHOPS:
        # Skip unsafe shops for key items
        if shop['id'] in UNSAFE_SHOPS_FOR_KEY_ITEMS:
            if verbose:
                print(f"Skipping shop {shop['id']} for Starstone placement due to offset conflict")
            continue
            
        # Skip shops in areas requiring Starstones
        shop_area = None
        for area_name, area_data in PROGRESSION_AREAS.items():
            if ('Starstone' in area_data['required'] or 'Starstones5' in area_data['required']) and shop['location'] in area_name:
                shop_area = area_name
                break
        
        if not shop_area:  # If shop isn't in a restricted area
            available_shops.append(shop)

    # Divide Starstones between chests and shops (3 in chests, 2 in shops is a good balance)
    chest_starstone_count = min(3, len(available_chests))
    shop_starstone_count = 5 - chest_starstone_count

    # Place Starstones in chests
    for i in range(chest_starstone_count):
        if i < len(available_chests):
            chest_id = available_chests[i]
            chest_contents[chest_id] = starstone_id
            used_chests.add(chest_id)
            starstone_count += 1
            
            # Get a valid location for the chest
            chest_location = "Unknown"
            if chest_id in CHEST_MAP:
                chest = CHEST_MAP[chest_id]
                chest_location = f"{chest.get('mapName', 'Unknown')} ({chest.get('posX', '?')},{chest.get('posY', '?')})"
            
            # Also track the location for the spoiler log
            starstone_locations.append({
                'type': 'chest',
                'location': chest_location,
                'chest_id': chest_id
            })
            
            if verbose:
                print(f"Placed Starstone #{starstone_count} in chest {chest_id} ({chest_location})")

    # Filter shops with available space for Starstones
    shops_with_space = []
    for shop in available_shops:
        shop_id = shop['id']
        
        current_count = shop_item_counts.get(shop_id, 0)
        max_items = get_max_shop_items(shop_id, options)
        
        # Only add shop if it has space
        if current_count < max_items:
            shops_with_space.append(shop)

    shuffle_array(shops_with_space)

    # Place remaining Starstones in shops
    for i in range(min(shop_starstone_count, len(shops_with_space))):
        shop = shops_with_space[i]
        shop_id = shop['id']
        
        if shop_id not in shop_contents:
            shop_contents[shop_id] = []
            shop_item_counts[shop_id] = 0
        
        # Add Starstone to shop with a higher price (since it's a key item)
        price = 400 + random.randint(0, 200)
        shop_contents[shop_id].append({
            'itemId': starstone_id,
            'name': 'Starstone',
            'type': ItemTypes.KEY_ITEM,
            'price': price,
            'bcdPrice': decimal_to_bcd(price),
            'limit': 1  # Limit to 1 purchase
        })
        
        # Update shop item count
        shop_item_counts[shop_id] = shop_item_counts.get(shop_id, 0) + 1
        
        # Also track the location for the spoiler log
        starstone_locations.append({
            'type': 'shop',
            'location': shop['location'],
            'price': price,
            'shop_id': shop_id
        })
        
        starstone_count += 1
        
        if verbose:
            print(f"Placed Starstone #{starstone_count} in shop {shop['location']} for {price} gems")

    # If we still can't place all the Starstones, fallback to any chest except Portrait
    while starstone_count < 5:
        remaining_chests = [chest_id for chest_id in CHEST_MAP.keys() 
                          if chest_id not in used_chests and chest_id != PORTRAIT_CHEST_ID]
        if not remaining_chests:
            # If we run out of chests, force placement by replacing a non-key item (but not Portrait)
            all_chests = [chest_id for chest_id in CHEST_MAP.keys() if chest_id != PORTRAIT_CHEST_ID]
            shuffle_array(all_chests)
            for chest_id in all_chests:
                if chest_id not in used_chests or chest_contents.get(chest_id) not in [ITEM_NAME_TO_ID.get(key) for key in PROGRESSION_KEY_ITEMS]:
                    chest_contents[chest_id] = starstone_id
                    used_chests.add(chest_id)
                    
                    # Get a valid location for the chest
                    chest_location = "Unknown"
                    if chest_id in CHEST_MAP:
                        chest = CHEST_MAP[chest_id]
                        chest_location = f"{chest.get('mapName', 'Unknown')} ({chest.get('posX', '?')},{chest.get('posY', '?')})"
                    
                    # Track it properly
                    starstone_locations.append({
                        'type': 'chest',
                        'location': chest_location,
                        'chest_id': chest_id
                    })
                    
                    starstone_count += 1
                    if verbose:
                        print(f"Placed Starstone #{starstone_count} in chest {chest_id} ({chest_location}) (forced placement)")
                    break
            
            if starstone_count >= 5:
                break
        else:
            shuffle_array(remaining_chests)
            chest_id = remaining_chests[0]
            chest_contents[chest_id] = starstone_id
            used_chests.add(chest_id)
            
            # Get a valid location for the chest
            chest_location = "Unknown"
            if chest_id in CHEST_MAP:
                chest = CHEST_MAP[chest_id]
                chest_location = f"{chest.get('mapName', 'Unknown')} ({chest.get('posX', '?')},{chest.get('posY', '?')})"
            
            # Track it properly
            starstone_locations.append({
                'type': 'chest',
                'location': chest_location,
                'chest_id': chest_id
            })
            
            starstone_count += 1
            if verbose:
                print(f"Placed Starstone #{starstone_count} in chest {chest_id} ({chest_location}) (fallback)")
                
        # Emergency break if we somehow can't place more
        if starstone_count < 5 and len(remaining_chests) == 0:
            if verbose:
                print(f"WARNING: Could only place {starstone_count}/5 Starstones even with fallbacks")
            return None
    
    # If we get here, we should have successfully placed all 5 Starstones
    if verbose:
        print(f"Successfully placed all 5 Starstones")
        for i, location in enumerate(starstone_locations):
            if location['type'] == 'chest':
                print(f"  Starstone #{i+1}: Chest in {location['location']}")
            else:
                print(f"  Starstone #{i+1}: Shop in {location['location']} ({location['price']} gems)")
    
    # Add a virtual "Starstones5" to collected_items to represent having all 5
    collected_items.add('Starstones5')
    
    # 8. Place the remaining key items based on game progression
    remaining_key_items = [item for item in PROGRESSION_KEY_ITEMS if item not in key_items_placed and item != 'Starstone']
    
    for key_item in remaining_key_items:
        # Get accessible areas with current items
        current_accessible_areas = get_accessible_areas(collected_items)
        current_accessible_chests = [chest_id for chest_id in get_accessible_chests(collected_items) 
                                   if chest_id not in used_chests]
        
        if verbose:
            print(f"For {key_item} placement - Accessible areas: {', '.join(current_accessible_areas)}")
            print(f"For {key_item} placement - Accessible chests: {len(current_accessible_chests)}")
        
        # Determine base price based on key item importance
        base_price = 200
        if key_item in ['Tower Key', 'Sewer Key', 'Starstone']:
            base_price = 400
        elif key_item in ['Magic Anchor', 'Speed Shoes']:
            base_price = 550
        elif key_item == 'Air Herb':
            base_price = 300
        
        if key_item_placements.get(key_item) == 'shop':
            # Determine appropriate shop tier based on key item
            available_shops = []
            
            if key_item in ['Tower Key', 'Sewer Key']:
                # These can be in early or mid shops
                available_shops = early_shops + mid_shops
            elif key_item in ['Starstone', 'Magic Anchor']:
                # These are generally mid to late game
                available_shops = mid_shops + late_shops
            else:
                # Others can be anywhere
                available_shops = early_shops + mid_shops + late_shops
            
            # Filter shops based on available space
            shops_with_space = []
            for shop in available_shops:
                shop_id = shop['id']
                current_count = shop_item_counts.get(shop_id, 0)
                max_items = get_max_shop_items(shop_id, options)
                
                if current_count < max_items:
                    shops_with_space.append(shop)
            
            if not place_item_in_shop(key_item, shops_with_space, base_price):
                # Fallback to chest placement
                if not place_item_in_chest(key_item, current_accessible_chests):
                    if verbose:
                        print(f"Failed to place {key_item}")
                    continue  # Skip this item - not all are essential
            
        else:
            # Place in chest
            if not place_item_in_chest(key_item, current_accessible_chests):
                # If no accessible chests, try shop placement as fallback
                available_shops = []
                
                if key_item in ['Tower Key', 'Sewer Key']:
                    base_shops = early_shops + mid_shops
                elif key_item in ['Starstone', 'Magic Anchor']:
                    base_shops = mid_shops + late_shops
                else:
                    base_shops = early_shops + mid_shops + late_shops
                
                # Filter shops with space
                for shop in base_shops:
                    shop_id = shop['id']
                    current_count = shop_item_counts.get(shop_id, 0)
                    max_items = get_max_shop_items(shop_id, options)
                    
                    if current_count < max_items:
                        available_shops.append(shop)
                
                if not place_item_in_shop(key_item, available_shops, base_price):
                    if verbose:
                        print(f"Failed to place {key_item}")
                    continue  # Skip this item - not all are essential
    
    # Verify the key items placements are complete
    essential_items = [
        'Giant Leaves', 'Ra Dewdrop', 'RocSpear', 'Sharp Claws', 'Crystal Thread', 'Holy Seal', 
        'Red Scarf', 'Protect Bell', 'Dog Whistle', 'Engagement Ring', 'Air Herb', 'Starstones5'
    ]
    for key_item in essential_items:
        if key_item not in collected_items:
            if verbose:
                print(f"Missing essential key item: {key_item}")
            return None
    
    # Get all unique weapons and armor
    unique_weapons = []
    unique_armor = []
    
    for id_hex, item in ITEM_DATABASE.items():
        if item['type'] == ItemTypes.WEAPON and int(id_hex, 16) not in placed_items:
            unique_weapons.append(int(id_hex, 16))
        elif item['type'] == ItemTypes.ARMOR and int(id_hex, 16) not in placed_items:
            unique_armor.append(int(id_hex, 16))
    
    # Shuffle these pools
    shuffle_array(unique_weapons)
    shuffle_array(unique_armor)
    
    # Place weapons (50% in chests, 50% in shops)
    weapons_in_chest = len(unique_weapons) // 2
    
    # Place weapons in chests (excluding Portrait chest)
    all_known_chest_ids = [chest_id for chest_id in CHEST_MAP.keys() if chest_id != PORTRAIT_CHEST_ID]
    remaining_chests = [chest_id for chest_id in all_known_chest_ids if chest_id not in used_chests]
    shuffle_array(remaining_chests)
    
    for i in range(min(weapons_in_chest, len(unique_weapons), len(remaining_chests))):
        chest_id = remaining_chests[i]
        item_id = unique_weapons[i]
        
        chest_contents[chest_id] = item_id
        used_chests.add(chest_id)
        placed_items.add(item_id)
    
    # Place remaining weapons in shops with space available
    weapons_for_shops = unique_weapons[weapons_in_chest:]
    all_shops = early_shops + mid_shops + late_shops
    shops_with_space = []
    
    # Check space in each shop
    for shop in all_shops:
        shop_id = shop['id']
        current_count = shop_item_counts.get(shop_id, 0)
        max_items = get_max_shop_items(shop_id, options)
        
        if current_count < max_items:
            shops_with_space.append((shop, max_items - current_count))  # (shop, available slots)
    
    # Sort by available space, descending
    shops_with_space.sort(key=lambda x: x[1], reverse=True)
    
    # Distribute weapons across shops based on game progress
    weapon_index = 0
    while weapon_index < len(weapons_for_shops) and shops_with_space:
        shop, slots = shops_with_space.pop(0)
        shop_id = shop['id']
        
        # Figure out how many weapons to add to this shop
        weapons_to_add = min(slots, len(weapons_for_shops) - weapon_index)
        
        for i in range(weapons_to_add):
            item_id = weapons_for_shops[weapon_index]
            item_hex = f"{item_id:04X}"
            item = ITEM_DATABASE.get(item_hex, {})
            
            if not item:
                weapon_index += 1
                continue
            
            if shop_id not in shop_contents:
                shop_contents[shop_id] = []
                shop_item_counts[shop_id] = 0
            
            # Calculate price based on game tier
            tier = get_progression_tier(shop['location'])
            price = calculate_item_price(item, tier, lambda: random.random(), {
                'randomize_prices': True,
                'price_variation': 30
            })
            
            shop_contents[shop_id].append({
                'itemId': item_id,
                'name': item['name'],
                'type': item['type'],
                'price': price,
                'bcdPrice': decimal_to_bcd(price),
                'limit': 1  # Limit to 1 purchase
            })
            
            # Update shop item count
            shop_item_counts[shop_id] = shop_item_counts.get(shop_id, 0) + 1
            
            placed_items.add(item_id)
            weapon_index += 1
    
    # Similar approach for armor - split between chests and shops
    armor_in_chest = len(unique_armor) // 2
    
    # Filter for remaining available chests (excluding Portrait)
    remaining_chests_for_armor = [chest_id for chest_id in remaining_chests if chest_id not in used_chests]
    
    # Place armor in chests
    for i in range(min(armor_in_chest, len(unique_armor), len(remaining_chests_for_armor))):
        chest_id = remaining_chests_for_armor[i]
        item_id = unique_armor[i]
        
        chest_contents[chest_id] = item_id
        used_chests.add(chest_id)
        placed_items.add(item_id)
    
    # Place remaining armor in shops with space
    armor_for_shops = unique_armor[armor_in_chest:]
    shops_with_space = []
    
    # Check space in each shop again after weapon placement
    for shop in all_shops:
        shop_id = shop['id']
        current_count = shop_item_counts.get(shop_id, 0)
        max_items = get_max_shop_items(shop_id, options)
        
        if current_count < max_items:
            shops_with_space.append((shop, max_items - current_count))  # (shop, available slots)
    
    # Sort by available space, descending
    shops_with_space.sort(key=lambda x: x[1], reverse=True)
    
    # Distribute armor across shops based on game progress
    armor_index = 0
    while armor_index < len(armor_for_shops) and shops_with_space:
        shop, slots = shops_with_space.pop(0)
        shop_id = shop['id']
        
        # Figure out how many armor pieces to add to this shop
        armor_to_add = min(slots, len(armor_for_shops) - armor_index)
        
        for i in range(armor_to_add):
            item_id = armor_for_shops[armor_index]
            item_hex = f"{item_id:04X}"
            item = ITEM_DATABASE.get(item_hex, {})
            
            if not item:
                armor_index += 1
                continue
            
            if shop_id not in shop_contents:
                shop_contents[shop_id] = []
                shop_item_counts[shop_id] = 0
            
            # Calculate price based on game tier
            tier = get_progression_tier(shop['location'])
            price = calculate_item_price(item, tier, lambda: random.random(), {
                'randomize_prices': True,
                'price_variation': 30
            })
            
            shop_contents[shop_id].append({
                'itemId': item_id,
                'name': item['name'],
                'type': item['type'],
                'price': price,
                'bcdPrice': decimal_to_bcd(price),
                'limit': 1  # Limit to 1 purchase
            })
            
            # Update shop item count
            shop_item_counts[shop_id] = shop_item_counts.get(shop_id, 0) + 1
            
            placed_items.add(item_id)
            armor_index += 1
    
    # Now add common items (consumables, rings) to fill remaining shops
    # These can have duplicates
    
    # Consumables are fine to duplicate
    consumables = []
    for id_hex, item in ITEM_DATABASE.items():
        if item['type'] == ItemTypes.CONSUMABLE:
            consumables.append(int(id_hex, 16))
    
    # Rings can have duplicates too
    rings = []
    for id_hex, item in ITEM_DATABASE.items():
        if item['type'] == ItemTypes.RING:
            rings.append(int(id_hex, 16))
    
    # Gems can have duplicates
    gems = []
    for id_hex, item in ITEM_DATABASE.items():
        if item['type'] == ItemTypes.GEMS:
            gems.append(int(id_hex, 16))
    
    # Now fill remaining chests with common items (excluding Portrait)
    final_remaining_chests = [chest_id for chest_id in all_known_chest_ids if chest_id not in used_chests]
    common_items = consumables + rings + gems
    shuffle_array(common_items)
    
    for i, chest_id in enumerate(final_remaining_chests):
        item_id = common_items[i % len(common_items)]  # Cycle through items if needed
        chest_contents[chest_id] = item_id
    
    # Fill shops with remaining common items based on their max capacity
    for shop in all_shops:
        shop_id = shop['id']
        current_count = shop_item_counts.get(shop_id, 0)
        max_items = get_max_shop_items(shop_id, options)
        
        # Skip if shop is already full
        if current_count >= max_items:
            continue
        
        # Skip if this shop doesn't have a shop contents entry yet
        if shop_id not in shop_contents:
            shop_contents[shop_id] = []
            shop_item_counts[shop_id] = 0
        
        # Determine how many more items to add to reach the target
        remaining_slots = max_items - current_count
        
        if remaining_slots <= 0:
            continue
            
        # Add consumables
        shuffle_array(consumables)
        for i in range(remaining_slots):
            if i >= len(consumables):
                break
                
            item_id = consumables[i % len(consumables)]
            item_hex = f"{item_id:04X}"
            item = ITEM_DATABASE.get(item_hex, {})
            
            if not item:
                continue
            
            # Standard price for consumables
            price = 0
            name = item['name']
            if name == 'S.Bulb':
                price = 10
            elif name == 'M.Bulb':
                price = 25
            elif name == 'L.Bulb':
                price = 70
            elif name == 'P. Cure':
                price = 13
            elif name == 'Stardew':
                price = 30
            elif name == 'Serum':
                price = 45
            elif name == 'H.Water':
                price = 90
            elif name == 'STR Potion':
                price = 110
            elif name == 'DEF Potion':
                price = 110
            elif name == 'Luck Potion':
                price = 130
            elif name == 'Life Potion':
                price = 150
            else:
                price = 25  # Default
            
            # Add some variation
            price = max(5, int(price * (0.85 + (random.random() * 0.3))))
            
            shop_contents[shop_id].append({
                'itemId': item_id,
                'name': item['name'],
                'type': item['type'],
                'price': price,
                'bcdPrice': decimal_to_bcd(price),
                'limit': 0  # No limit on consumables
            })
            
            # Update shop item count
            shop_item_counts[shop_id] = shop_item_counts.get(shop_id, 0) + 1
            
            # If we've reached the max items for this shop, break
            if shop_item_counts[shop_id] >= max_items:
                break
    
    # Verify the placement works correctly
    if validate_game_progress(chest_contents, shop_contents, verbose):
        if verbose:
            print("Placement validated - game is beatable!")
            print(f"Portrait chest {PORTRAIT_CHEST_ID} protected with item {PORTRAIT_ITEM_ID}")
        return {
            'chest_contents': chest_contents,
            'shop_contents': shop_contents,
            'key_item_placements': key_item_placements,
            'starstone_locations': starstone_locations
        }
    else:
        if verbose:
            print("Placement validation failed - game is not beatable!")
        return None

def randomize_shops_with_key_items(rom_data, options, shop_contents):
    """
    Modified shop randomization function that incorporates key item integration
    and handles shop evolution conflicts
    
    Args:
        rom_data (bytearray): ROM buffer
        options (dict): Randomization options
        shop_contents (dict): Map of shop IDs to items
        
    Returns:
        dict: Modified ROM buffer and randomized shops
    """
    print('\nRandomizing shops with unique item integration...')
    
    # IMPORTANT: Preserve key items across evolution groups FIRST
    print("Preserving key items across shop evolution stages...")
    shop_contents = preserve_key_items_across_evolution(shop_contents)
    
    # THEN handle shared offset conflicts (non-evolution)
    shop_contents = handle_shared_offset_shops(shop_contents)
    
    # Read shop data using our known addresses
    shops = read_shops_from_rom(rom_data)
    print(f"Using {len(shops)} shops from the known shops database.")
    
    # Create RNG with seed
    rng = create_seeded_rng(options.get('seed', random.randint(0, 999999)))
    
    # Add items to shops according to the placements
    for shop_id_str, items in shop_contents.items():
        # Convert string shop_id to int if necessary
        try:
            shop_id = int(shop_id_str) if isinstance(shop_id_str, str) else shop_id_str
        except ValueError:
            print(f"WARNING: Invalid shop ID format: {shop_id_str}")
            continue
            
        shop_index = -1
        for i, shop in enumerate(shops):
            if shop['id'] == shop_id:
                shop_index = i
                break
                
        if shop_index != -1:
            # Replace shop's items with our planned items
            shops[shop_index]['items'] = items
            
            if options.get('verbose', False):
                key_items = []
                evolution_group, stage = get_evolution_group(shop_id)
                
                for item in items:
                    item_name = get_item_name(item['itemId'])
                    if item_name in PROGRESSION_KEY_ITEMS:
                        key_items.append(item)
                
                shop_location_info = f"{shops[shop_index]['location']}"
                if evolution_group:
                    shop_location_info += f" (Evolution group: {evolution_group}, Stage: {stage})"
                
                if key_items:
                    print(f"Added {len(key_items)} key items to shop #{shop_id} ({shop_location_info})")
                    for item in key_items:
                        print(f"  - {get_item_name(item['itemId'])}: {item['price']} gems (limit: {item['limit']})")
        else:
            print(f"WARNING: Shop ID {shop_id} not found in loaded shops - skipping")
    
    # Validate prices and item counts
    validate_shop_prices(shops)
    validate_shop_item_counts(shops)
    
    # Write changes back to the ROM
    modified_rom = write_shops_to_rom(rom_data, shops)
    
    return {
        'rom': modified_rom,
        'shops': shops
    }

def randomize_with_unique_items(rom_data, options):
    """
    Modified main randomizer function that enforces unique items across the game world
    and handles shop evolution conflicts by preserving key items across evolution stages
    IMPORTANT: Protects Portrait chest from randomization
    
    Args:
        rom_data (bytearray): ROM buffer
        options (dict): Randomization options
        
    Returns:
        dict: Modified ROM buffer, spoiler log, etc.
    """
    print('\nRandomizing with unique item constraints and shop evolution support...')
    print(f'NOTE: Portrait chest ({PORTRAIT_CHEST_ID}) will remain in vanilla location')
    print('Key items will persist across shop evolution stages')
    
    # Create logical placement of items in both chests and shops
    placement = None
    attempts = 0
    max_attempts = options.get('max_attempts', 100)
    
    while attempts < max_attempts:
        attempts += 1
        if options.get('verbose', False):
            print(f"Attempt {attempts}/{max_attempts} to create logical placement...")
        
        placement = create_enhanced_logical_placement(options.get('verbose', False), options)
        if placement:
            break
    
    if not placement:
        print(f"Failed to create logical placement after {max_attempts} attempts.")
        return { 
            'rom': rom_data, 
            'success': False,
            'error': "Could not create a valid logical placement" 
        }
    
    print(f"Created logical placement with unique items after {attempts} attempt(s).")
    
    # Extract the chest contents and shop placements
    chest_contents = placement['chest_contents']
    shop_contents = placement['shop_contents']
    key_item_placements = placement['key_item_placements']
    
    # Verify Portrait chest is protected
    if PORTRAIT_CHEST_ID not in chest_contents or chest_contents[PORTRAIT_CHEST_ID] != PORTRAIT_ITEM_ID:
        print(f"ERROR: Portrait chest protection failed! Expected {PORTRAIT_ITEM_ID}, got {chest_contents.get(PORTRAIT_CHEST_ID)}")
        return {
            'rom': rom_data,
            'success': False,
            'error': "Portrait chest protection failed"
        }
    
    if options.get('verbose', False):
        print(f"Confirmed Portrait chest {PORTRAIT_CHEST_ID} protected with item {PORTRAIT_ITEM_ID}")
    
    # Initialize starstone_locations - either from the placement or as an empty list
    starstone_locations = placement.get('starstone_locations', [])
    
    # Read current chest data for spoiler log
    current_chests = read_chests_from_rom(rom_data)
    
    # DEBUG: Print contents of shop_contents
    if options.get('verbose', False):
        print("\nDEBUG: Shop contents to be written:")
        for shop_id, items in shop_contents.items():
            evolution_group, stage = get_evolution_group(int(shop_id) if isinstance(shop_id, str) else shop_id)
            group_info = f" (Group: {evolution_group}, Stage: {stage})" if evolution_group else ""
            print(f"  Shop {shop_id}{group_info}: {len(items)} items")
            for item in items:
                print(f"    - {item['name']} (ID: {item['itemId']}, Price: {item['price']})")
    
    # Randomize chests with the logical placement
    modified_rom = write_chests_to_rom(rom_data, chest_contents)
    
    # Randomize shops with key items integrated
    shop_result = randomize_shops_with_key_items(modified_rom, options, shop_contents)
    final_rom = shop_result['rom']
    randomized_shops = shop_result['shops']
    
    # Create combined spoiler log
    chest_spoiler_log = []
    for chest in current_chests:
        new_item_id = chest_contents.get(chest['id'], chest['itemID'])
        new_item_name = get_item_name(new_item_id)
        
        entry = {
            'chestID': chest['id'],
            'location': f"{chest['mapName'] if 'mapName' in chest else 'Unknown'} ({chest['posX']},{chest['posY']})",
            'originalItem': chest['itemName'],
            'originalItemId': chest['itemID'],
            'newItem': new_item_name,
            'newItemId': new_item_id
        }
        
        # Add note for Portrait
        if chest['id'] == PORTRAIT_CHEST_ID:
            entry['note'] = 'NOT RANDOMIZED - Vanilla location due to Storkolm entry bug'
        
        chest_spoiler_log.append(entry)
    
    # Create an enhanced spoiler log that also shows key items in shops
    key_items_in_shops = []
    unique_items_in_shops = []
    
    # Process all shop items for key items and unique weapons/armor
    for shop in randomized_shops:
        evolution_group, stage = get_evolution_group(shop['id'])
        
        for item in shop['items']:
            item_name = get_item_name(item['itemId'])
            item_hex = f"{item['itemId']:04X}"
            item_info = ITEM_DATABASE.get(item_hex, {})
            
            # Track key items
            if item_name in PROGRESSION_KEY_ITEMS:
                key_items_in_shops.append({
                    'shopID': shop['id'],
                    'location': shop['location'],
                    'evolutionGroup': evolution_group,
                    'stage': stage,
                    'item': item_name,
                    'price': item['price'],
                    'limit': item['limit'],
                    'type': item_info.get('type', "KEY_ITEM")
                })
            
            # Also track unique weapons and armor
            if (item_info.get('type') == ItemTypes.WEAPON or item_info.get('type') == ItemTypes.ARMOR) and item['limit'] > 0:
                unique_items_in_shops.append({
                    'shopID': shop['id'],
                    'location': shop['location'],
                    'evolutionGroup': evolution_group,
                    'stage': stage,
                    'item': item_name,
                    'price': item['price'],
                    'limit': item['limit'],
                    'type': item_info.get('type')
                })
    
    # Verify we have 5 Starstones
    if len(starstone_locations) < 5:
        print(f"WARNING: Only {len(starstone_locations)}/5 Starstones were placed.")
        
        # Count Starstones in chest contents and shops to debug
        starstone_id = ITEM_NAME_TO_ID.get('Starstone')
        chest_starstone_count = sum(1 for _, item_id in chest_contents.items() if item_id == starstone_id)
        shop_starstone_count = sum(1 for shop_id, items in shop_contents.items() 
                                  for item in items if item['itemId'] == starstone_id)
        
        print(f"Starstones in chest_contents: {chest_starstone_count}")
        print(f"Starstones in shop_contents: {shop_starstone_count}")
        
        # Try to recover missing Starstones
        for chest_id, item_id in chest_contents.items():
            if item_id == starstone_id:
                # Check if this chest is already in starstone_locations
                already_tracked = any(loc['type'] == 'chest' and loc.get('chest_id') == chest_id 
                                     for loc in starstone_locations)
                
                if not already_tracked:
                    # Get chest location
                    chest_location = "Unknown"
                    if chest_id in CHEST_MAP:
                        chest = CHEST_MAP[chest_id]
                        chest_location = f"{chest.get('mapName', 'Unknown')} ({chest.get('posX', '?')},{chest.get('posY', '?')})"
                    
                    # Add to tracking
                    starstone_locations.append({
                        'type': 'chest',
                        'location': chest_location,
                        'chest_id': chest_id
                    })
                    print(f"Recovered missing Starstone in chest {chest_id} at {chest_location}")
        
        # Check for Starstones in shops that might not be tracked
        for shop_id, items in shop_contents.items():
            for item in items:
                if item['itemId'] == starstone_id:
                    # Find corresponding shop
                    shop_info = next((shop for shop in randomized_shops if shop['id'] == int(shop_id)), None)
                    
                    if shop_info:
                        # Check if this shop is already in starstone_locations
                        already_tracked = any(loc['type'] == 'shop' and loc.get('shop_id') == shop_id 
                                             for loc in starstone_locations)
                        
                        if not already_tracked:
                            # Add to tracking
                            starstone_locations.append({
                                'type': 'shop',
                                'location': shop_info['location'],
                                'price': item['price'],
                                'shop_id': shop_id
                            })
                            print(f"Recovered missing Starstone in shop {shop_id} at {shop_info['location']}")
        
        # Total Starstones after recovery attempts
        total_starstones = len(starstone_locations)
        
        # If we still don't have 5 Starstones, this seed is invalid
        if total_starstones < 5:
            print(f"FATAL ERROR: Only found {total_starstones}/5 required Starstones. This seed is invalid.")
            return {
                'rom': rom_data,
                'success': False,
                'error': f"Could not place all 5 Starstones (found {total_starstones})"
            }
    else:
        print(f"Successfully placed all 5 Starstones:")
        for i, location in enumerate(starstone_locations):
            if location['type'] == 'chest':
                print(f"  - Starstone #{i+1}: Chest in {location['location']}")
            else:
                print(f"  - Starstone #{i+1}: Shop in {location['location']} ({location['price']} gems)")
    
    # Additional verification of shop contents
    # Read shops from the final ROM to verify they were properly written
    final_shops = read_shops_from_rom(final_rom)
    print("\nVerifying shop contents after randomization:")
    
    key_items_found = 0
    evolution_groups_with_key_items = {}
    
    for shop in final_shops:
        shop_id = shop['id']
        evolution_group, stage = get_evolution_group(shop_id)
        
        # Count key items in this shop using the name field directly
        key_items_in_shop = []
        for item in shop['items']:
            # Use the name field directly instead of calling get_item_name
            if item.get('name') in PROGRESSION_KEY_ITEMS:
                key_items_in_shop.append(item)
        
        if key_items_in_shop:
            key_items_found += len(key_items_in_shop)
            group_info = f" (Evolution group: {evolution_group}, Stage: {stage})" if evolution_group else ""
            print(f"  Shop {shop_id} ({shop['location']}{group_info}): {len(key_items_in_shop)} key items found")
            for item in key_items_in_shop:
                print(f"    - {item['name']} (ID: {item['itemId']}, Price: {item['price']})")
            
            # Track evolution groups with key items
            if evolution_group:
                if evolution_group not in evolution_groups_with_key_items:
                    evolution_groups_with_key_items[evolution_group] = {}
                evolution_groups_with_key_items[evolution_group][shop_id] = key_items_in_shop
    
    print(f"Total key items found in shops: {key_items_found}")
    
    # Verify key items are preserved across evolution groups
    print("\nVerifying key item preservation across evolution groups:")
    for group_name, shops_dict in evolution_groups_with_key_items.items():
        group_key_items = set()
        for shop_id, items in shops_dict.items():
            for item in items:
                group_key_items.add(item['name'])
        
        print(f"  {group_name}: {len(group_key_items)} unique key items across {len(shops_dict)} stages")
        if len(shops_dict) > 1:
            # Check that all shops in the group have the same key items
            first_shop_items = set(item['name'] for item in list(shops_dict.values())[0])
            all_match = all(
                set(item['name'] for item in items) == first_shop_items 
                for items in shops_dict.values()
            )
            if all_match:
                print(f"    [OK] All stages have the same key items")
            else:
                print(f"    [WARN] WARNING: Key items differ between stages!")
    
    return {
        'rom': final_rom,
        'chest_spoiler_log': chest_spoiler_log,
        'shop_spoiler_log': randomized_shops,
        'key_items_in_shops': key_items_in_shops,
        'unique_items_in_shops': unique_items_in_shops,
        'key_item_placements': key_item_placements,
        'starstone_locations': starstone_locations,
        'success': True
    }

def randomize_with_shop_integration(rom_data, options):
    """
    Main randomizer function with integrated logic for chest and shop randomization
    Includes support for shop evolution conflicts
    IMPORTANT: Protects Portrait chest from randomization
    
    Args:
        rom_data (bytearray): ROM buffer
        options (dict): Randomization options
        
    Returns:
        dict: Modified ROM buffer, spoiler logs, etc.
    """
    # Similar to randomize_with_unique_items but without enforcing uniqueness
    # For now, just use the same implementation with shop evolution support
    return randomize_with_unique_items(rom_data, options)    