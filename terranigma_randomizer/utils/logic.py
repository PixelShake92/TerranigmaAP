"""
Game logic functions for Terranigma Randomizer
Functions for determining accessible areas, item placement, etc.
"""

import random
from terranigma_randomizer.constants.items import ITEM_NAME_TO_ID, PROGRESSION_KEY_ITEMS, PORTRAIT_CHEST_ID, PORTRAIT_ITEM_ID
from terranigma_randomizer.constants.progression import (
    get_accessible_areas, get_accessible_chests, get_accessible_shops,
    KEY_ITEM_GATES, SHOP_ID_TO_NAME, SHOP_NAME_TO_ID, PROGRESSION_AREAS
)
from terranigma_randomizer.constants.chests import CHEST_MAP, KNOWN_CHESTS
from terranigma_randomizer.constants.shops import KNOWN_SHOPS, SHOP_ID_TO_INDEX, decimal_to_bcd

# Define key progression points
KEY_PROGRESSION_POINTS = {
    'Giant Leaves': {
        'description': 'Must be obtained before accessing the surface world',
        'required_before': ['SURFACE_INITIAL', 'GRECLIFF_ENTRANCE'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'SHOP_CRYSTA_DAY', 'SHOP_CRYSTA_NIGHT']
    },
    'Ra Dewdrop': {
        'description': 'Must be obtained before fighting Ra Tree Boss',
        'required_before': ['TREE_CAVE_INNER'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'SHOP_CRYSTA_DAY', 'SHOP_CRYSTA_NIGHT']
    },
    'RocSpear': {
        'description': 'Must be obtained before accessing mid-Grecliff',
        'required_before': ['GRECLIFF_MIDDLE'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'SHOP_CRYSTA_DAY', 'SHOP_CRYSTA_NIGHT', 'SHOP_LUMINA_1']
    },
    'Sharp Claws': {
        'description': 'Must be obtained before the Grecliff Boss',
        'required_before': ['GRECLIFF_BOSS'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'SHOP_LUMINA_1', 'SHOP_LUMINA_2', 'SHOP_SANCTUAR_BIRDS', 'SHOP_SANCTUAR_PRE', 'SHOP_SAFARIUM']
    },
    'Crystal Thread': {
        'description': 'Must be obtained before getting ElleCape',
        'required_before': ['ELLE_CAPE_AREA'],
        'can_place_in': ['UNDERWORLD_START', 'SHOP_CRYSTA_DAY']
    },
    'Snowgrass Leaf': {
        'description': 'Must be obtained before accessing Louran',
        'required_before': ['EKLEMATA_REGION'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'SHOP_LUMINA_1', 'SHOP_LUMINA_2', 'SHOP_SANCTUAR_BIRDS', 'SHOP_SANCTUAR_PRE', 'SHOP_SAFARIUM']
    },
    'Red Scarf': {
        'description': 'Must be obtained before accessing Louran',
        'required_before': ['LOURAN_REGION'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'LOURAN_REGION', 'SHOP_LUMINA_1', 'SHOP_LUMINA_2', 'SHOP_SANCTUAR_BIRDS', 'SHOP_SANCTUAR_PRE', 'SHOP_SAFARIUM', 'SHOP_INDUS_RIVER']
    },
    'Dog Whistle': {
        'description': 'Must be obtained before accessing Storkolm',
        'required_before': ['STORKOLM_REGION'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'SHOP_LUMINA_1', 'SHOP_LUMINA_2', 'SHOP_SANCTUAR_BIRDS', 'SHOP_SANCTUAR_PRE', 'SHOP_SAFARIUM', 'SHOP_LHASE', 'SHOP_LOIRE']
    },
    'Tower Key': {
        'description': 'Must be obtained before accessing Dragoon Castle',
        'required_before': ['DRAGOON_CASTLE'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'SYLVAIN_CASTLE', 'SHOP_LHASE', 'SHOP_LOIRE', 'SHOP_LOURAN']
    },
    'Magic Anchor': {
        'description': 'Must be obtained before accessing Mu',
        'required_before': ['MU_REGION', 'GREAT_LAKES_CAVERN'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'STORKOLM_REGION', 'SYLVAIN_CASTLE', 'DRAGOON_CASTLE', 'LOIRE_CASTLE', 'NEOTOKYO_SEWER', 'SHOP_FREEDOM_WEAPONS', 'SHOP_FREEDOM_ARMOR']
    },
    'Sewer Key': {
        'description': 'Must be obtained before accessing Sewers',
        'required_before': ['NEOTOKYO_SEWER'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'STORKOLM_REGION', 'SYLVAIN_CASTLE', 'DRAGOON_CASTLE', 'LOIRE_CASTLE', 'SHOP_LHASE', 'SHOP_LOIRE', 'SHOP_LOURAN']
    },
    'Air Herb': {
        'description': 'Must be obtained before accessing underwater areas',
        'required_before': ['GREAT_LAKES_CAVERN'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'STORKOLM_REGION', 'SYLVAIN_CASTLE', 'DRAGOON_CASTLE', 'LOIRE_CASTLE', 'NEOTOKYO_SEWER', 'MU_REGION', 'SHOP_FREEDOM_WEAPONS', 'SHOP_FREEDOM_ARMOR']
    },
    'Speed Shoes': {
        'description': 'Must be obtained before accessing hidden areas',
        'required_before': ['HIDDEN_REGIONS'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'STORKOLM_REGION', 'SYLVAIN_CASTLE', 'DRAGOON_CASTLE', 'LOIRE_CASTLE', 'NEOTOKYO_SEWER', 'MU_REGION', 'MERMAID_TOWER_REGION', 'SHOP_FREEDOM_WEAPONS', 'SHOP_FREEDOM_ARMOR', 'SHOP_SUNCOAST']
    },
    'Protect Bell': {
        'description': 'Must be obtained before accessing Norfest',
        'required_before': ['NORFEST_REGION'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'SHOP_LUMINA_1', 'SHOP_LUMINA_2', 'SHOP_SANCTUAR_BIRDS', 'SHOP_SANCTUAR_PRE', 'SHOP_SAFARIUM']
    },
    'Ruby': {
        'description': 'Must be obtained before accessing Sylvain Castle',
        'required_before': ['SYLVAIN_CASTLE'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'SHOP_LHASE', 'SHOP_LOIRE', 'SHOP_LOURAN']
    },
    'Sapphire': {
        'description': 'Must be obtained before accessing Sylvain Castle',
        'required_before': ['SYLVAIN_CASTLE'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'SHOP_LHASE', 'SHOP_LOIRE', 'SHOP_LOURAN']
    },
    'Black Opal': {
        'description': 'Must be obtained before accessing Sylvain Castle',
        'required_before': ['SYLVAIN_CASTLE'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'SHOP_LHASE', 'SHOP_LOIRE', 'SHOP_LOURAN']
    },
    'Topaz': {
        'description': 'Must be obtained before accessing Sylvain Castle',
        'required_before': ['SYLVAIN_CASTLE'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'SHOP_LHASE', 'SHOP_LOIRE', 'SHOP_LOURAN']
    },
    'Engagement Ring': {
        'description': 'Must be obtained before accessing Great Lakes Cavern',
        'required_before': ['GREAT_LAKES_CAVERN'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'STORKOLM_REGION', 'SYLVAIN_CASTLE', 'DRAGOON_CASTLE', 'LOIRE_CASTLE', 'NEOTOKYO_SEWER', 'MU_REGION', 'SHOP_FREEDOM_WEAPONS', 'SHOP_FREEDOM_ARMOR', 'SHOP_RING']
    },
    'Transceiver': {
        'description': 'Must be obtained before accessing Neo-Tokyo advanced areas',
        'required_before': ['NEOTOKYO_ADVANCED'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'STORKOLM_REGION', 'SYLVAIN_CASTLE', 'DRAGOON_CASTLE', 'LOIRE_CASTLE', 'NEOTOKYO_SEWER', 'SHOP_FREEDOM_WEAPONS', 'SHOP_FREEDOM_ARMOR']
    },
    'Starstone': {
        'description': 'Must obtain 5 of these before accessing Astarica',
        'required_before': ['ASTARICA_REGION'],
        'can_place_in': ['NEOTOKYO_SEWER', 'MU_REGION', 'GREAT_LAKES_CAVERN',
                          'SHOP_FREEDOM_WEAPONS', 'SHOP_FREEDOM_ARMOR', 'SHOP_SUNCOAST', 'SHOP_SUNCOAST_MAGIC']
    },
    'Time Bomb': {
        'description': 'Must be obtained before accessing Beruga Airship',
        'required_before': ['BERUGA_AIRSHIP'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'STORKOLM_REGION', 'SYLVAIN_CASTLE', 'DRAGOON_CASTLE', 'LOIRE_CASTLE', 'NEOTOKYO_SEWER', 'MU_REGION', 'MERMAID_TOWER_REGION', 'SHOP_FREEDOM_WEAPONS', 'SHOP_FREEDOM_ARMOR', 'SHOP_SUNCOAST']
    },
    'Ginseng': {
        'description': 'Must be obtained before healing Fyda',
        'required_before': ['FYDA_RECOVERY'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'STORKOLM_REGION', 'SYLVAIN_CASTLE', 'DRAGOON_CASTLE', 'LOIRE_CASTLE', 'NEOTOKYO_SEWER', 'MU_REGION', 'MERMAID_TOWER_REGION', 'SHOP_FREEDOM_WEAPONS', 'SHOP_FREEDOM_ARMOR', 'SHOP_SUNCOAST']
    },
    'Holy Seal': {
        'description': 'Must be obtained before facing Dark Gaia',
        'required_before': ['DARK_GAIA'],
        'can_place_in': ['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE', 'TREE_CAVE_INNER', 'SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'LOURAN_REGION', 'STORKOLM_REGION', 'SYLVAIN_CASTLE', 'DRAGOON_CASTLE', 'LOIRE_CASTLE', 'NEOTOKYO_SEWER', 'MU_REGION', 'MERMAID_TOWER_REGION', 'SHOP_FREEDOM_WEAPONS', 'SHOP_FREEDOM_ARMOR', 'SHOP_SUNCOAST']
    }
}

def shuffle_array(array):
    """
    Shuffle an array in-place using the Fisher-Yates algorithm
    
    Args:
        array (list): Array to shuffle
        
    Returns:
        list: The same array, shuffled
    """
    for i in range(len(array) - 1, 0, -1):
        j = random.randint(0, i)
        array[i], array[j] = array[j], array[i]
    return array

def create_seeded_rng(seed):
    """
    Create a seeded random number generator
    
    Args:
        seed (int): Random seed
        
    Returns:
        function: Random number generator
    """
    random.seed(seed)
    return lambda: random.random()

def get_chests_for_regions(regions):
    """
    Get all chest IDs in the given regions
    
    Args:
        regions (list): List of region names
        
    Returns:
        list: List of chest IDs
    """
    chest_ids = []
    for region in regions:
        if region in PROGRESSION_AREAS:
            chest_ids.extend(PROGRESSION_AREAS[region]['contains'])
    
    # Remove Portrait chest from the list
    if PORTRAIT_CHEST_ID in chest_ids:
        chest_ids.remove(PORTRAIT_CHEST_ID)
    
    return chest_ids

def get_shops_for_regions(regions):
    """
    Get all shop IDs in the given regions
    
    Args:
        regions (list): List of shop region identifiers
        
    Returns:
        list: List of shop IDs
    """
    shop_ids = []
    for region in regions:
        if region.startswith('SHOP_'):
            shop_ids.append(region)
    
    return shop_ids

def validate_game_progress(chest_contents, shop_contents, verbose=False):
    """
    Check if a randomized game is beatable by simulating progression
    
    Args:
        chest_contents (dict): Map of chest IDs to item IDs
        shop_contents (dict): Map of shop IDs to item arrays
        verbose (bool): Whether to log detailed information
        
    Returns:
        bool: True if game is beatable, false otherwise
    """
    # Start with no items
    collected_items = set()
    collected_gems = 1000  # Starting gems
    starstone_count = 0  # Track number of Starstones collected
    progress = True
    
    # Keep track of collected items for iteration
    item_count = 0
    
    # Simulate collecting items until we can't make progress
    while progress:
        if verbose:
            print(f"Iteration with {len(collected_items)} items collected")
        
        # Store item count to check for progress
        item_count = len(collected_items)
        
        # Get accessible areas and chests with current items
        accessible_areas = get_accessible_areas(collected_items)
        accessible_chests = get_accessible_chests(collected_items)
        accessible_shops = get_accessible_shops(collected_items)
        
        if verbose:
            print(f"Accessible areas: {', '.join(accessible_areas)}")
            print(f"Accessible chests: {len(accessible_chests)}")
            print(f"Accessible shops: {len(accessible_shops)}")
        
        # Collect items from accessible chests
        for chest_id in accessible_chests:
            if chest_id in chest_contents:
                item_id = chest_contents[chest_id]
                from terranigma_randomizer.constants.items import get_item_name
                item_name = get_item_name(item_id)
                
                # Special handling for Starstones
                if item_name == 'Starstone':
                    starstone_count += 1
                    if verbose:
                        print(f"Collected Starstone #{starstone_count} from chest {chest_id}")
                    
                    # Add a "virtual" item to track having enough Starstones
                    if starstone_count >= 5 and 'Starstones5' not in collected_items:
                        collected_items.add('Starstones5')
                        if verbose:
                            print(f"Collected enough Starstones (5) to access Astarica")
                
                # Add to collected items if it's a key item
                elif item_name in PROGRESSION_KEY_ITEMS and item_name not in collected_items:
                    collected_items.add(item_name)
                    if verbose:
                        print(f"Collected {item_name} from chest {chest_id}")
                
                # Check for gems
                from terranigma_randomizer.constants.items import get_item_info
                item_info = get_item_info(item_id)
                if item_info.get('type') == 'gems':
                    gem_value = item_info.get('value', 0)
                    collected_gems += gem_value
                    if verbose:
                        print(f"Collected {gem_value} gems from chest {chest_id}")
        
        # Collect items from accessible shops
        for shop_id in accessible_shops:
            if shop_id in shop_contents:
                shop_items = shop_contents[shop_id]
                
                # Shop items are represented as dicts with itemId and price
                for item in shop_items:
                    from terranigma_randomizer.constants.items import get_item_name
                    item_name = get_item_name(item['itemId'])
                    
                    # Special handling for Starstones
                    if item_name == 'Starstone':
                        # Check if we can afford it
                        if collected_gems >= item['price']:
                            starstone_count += 1
                            collected_gems -= item['price']
                            if verbose:
                                shop_name = SHOP_ID_TO_NAME.get(shop_id, shop_id)
                                print(f"Purchased Starstone #{starstone_count} from shop {shop_name} for {item['price']} gems")
                            
                            # Add a "virtual" item to track having enough Starstones
                            if starstone_count >= 5 and 'Starstones5' not in collected_items:
                                collected_items.add('Starstones5')
                                if verbose:
                                    print(f"Collected enough Starstones (5) to access Astarica")
                    
                    # Only consider key items
                    elif item_name in PROGRESSION_KEY_ITEMS and item_name not in collected_items:
                        # Check if we can afford it
                        if collected_gems >= item['price']:
                            collected_items.add(item_name)
                            collected_gems -= item['price']
                            if verbose:
                                shop_name = SHOP_ID_TO_NAME.get(shop_id, shop_id)
                                print(f"Purchased {item_name} from shop {shop_name} for {item['price']} gems")
                        else:
                            if verbose:
                                print(f"Can't afford {item_name} ({item['price']} gems) with {collected_gems} gems")
        
        # Check if we've made progress
        progress = len(collected_items) > item_count
    
    # Check if we've collected all required items for major progression
    essential_items = [
        'Giant Leaves', 
        'Ra Dewdrop', 
        'RocSpear', 
        'Sharp Claws',
        'Crystal Thread',
        'Red Scarf',
        'Protect Bell',
        'Dog Whistle',
        'Magic Anchor',
        'Starstones5'  # Add this to verify we have enough Starstones
    ]
    has_essential_items = all(item in collected_items for item in essential_items)
    
    if verbose:
        print('\nValidation results:')
        print(f"Total items collected: {len(collected_items)}")
        print(f"Essential items collected: {'Yes' if has_essential_items else 'No'}")
        print(f"Starstones collected: {starstone_count}/5")
        print('Collected items:', ', '.join(collected_items))
        missing_items = [item for item in essential_items if item not in collected_items]
        if missing_items:
            print('Missing essential items:', ', '.join(missing_items))
    
    return has_essential_items

def get_chest_location_name(chest_id):
    """
    Get a readable location name for a chest ID
    
    Args:
        chest_id (int or str): Chest ID
        
    Returns:
        str: Location name
    """
    # Convert string to int if needed
    if isinstance(chest_id, str) and chest_id.isdigit():
        chest_id = int(chest_id)
    
    # Try to find the chest
    if chest_id in CHEST_MAP:
        chest = CHEST_MAP[chest_id]
        return f"{chest.get('mapName', 'Unknown')} ({chest.get('posX', '?')},{chest.get('posY', '?')})"
    
    # Debug info
    print(f"DEBUG: Chest ID {chest_id} (type: {type(chest_id)}) not found in CHEST_MAP")
    
    # Check for similar IDs (in case of type issues)
    if isinstance(chest_id, int) and str(chest_id) in CHEST_MAP:
        chest = CHEST_MAP[str(chest_id)]
        return f"{chest.get('mapName', 'Unknown')} ({chest.get('posX', '?')},{chest.get('posY', '?')})"
    elif isinstance(chest_id, str) and int(chest_id) in CHEST_MAP:
        chest = CHEST_MAP[int(chest_id)]
        return f"{chest.get('mapName', 'Unknown')} ({chest.get('posX', '?')},{chest.get('posY', '?')})"
    
    return f"Unknown (Chest ID: {chest_id})"

def place_key_item_in_valid_region(key_item, collected_items, chest_contents, shop_contents, used_chests, used_shop_slots, verbose=False):
    """
    Place a key item in a valid accessible region (chest or shop)
    
    Args:
        key_item (str): Key item name
        collected_items (set): Currently collected items
        chest_contents (dict): Current chest contents mapping
        shop_contents (dict): Current shop contents mapping
        used_chests (set): Chests that have already been used
        used_shop_slots (dict): Shop slots that have already been used
        verbose (bool): Whether to print verbose output
        
    Returns:
        tuple: (success, location_type, location_id, item_id) - success is bool, location_type ('chest' or 'shop'), location_id and item_id if placed
    """
    item_id = ITEM_NAME_TO_ID.get(key_item)
    if not item_id:
        if verbose:
            print(f"Missing ID for item: {key_item}")
        return False, None, None, None
    
    # Get valid placement regions
    valid_regions = KEY_PROGRESSION_POINTS.get(key_item, {}).get('can_place_in', [])
    
    # If no specific regions defined, use base logic
    if not valid_regions:
        accessible_chests = get_accessible_chests(collected_items)
        available_chests = [chest_id for chest_id in accessible_chests if chest_id not in used_chests and chest_id != PORTRAIT_CHEST_ID]
        
        if not available_chests:
            if verbose:
                print(f"No accessible chests available for {key_item}")
            return False, None, None, None
        
        # Choose a random chest
        shuffle_array(available_chests)
        chosen_chest_id = available_chests[0]
        
        return True, 'chest', chosen_chest_id, item_id
    
    # Separate shop and chest regions
    chest_regions = [r for r in valid_regions if not r.startswith('SHOP_')]
    shop_regions = [r for r in valid_regions if r.startswith('SHOP_')]
    
    # Randomly decide whether to place in chest or shop (if both are available)
    place_in_shop = random.random() < 0.3 and shop_regions  # 30% chance to use shop if available
    
    if place_in_shop:
        # Filter for shops that are in the valid regions and have slots available
        available_shop_ids = []
        for shop_id in shop_regions:
            if shop_id not in used_shop_slots or used_shop_slots[shop_id] < 4:  # Limit 4 items per shop
                available_shop_ids.append(shop_id)
        
        if available_shop_ids:
            shuffle_array(available_shop_ids)
            chosen_shop_id = available_shop_ids[0]
            
            # Track used shop slots
            if chosen_shop_id not in used_shop_slots:
                used_shop_slots[chosen_shop_id] = 1
            else:
                used_shop_slots[chosen_shop_id] += 1
            
            return True, 'shop', chosen_shop_id, item_id
    
    # Get all chests in the valid regions
    valid_chests = get_chests_for_regions(chest_regions)
    
    # Filter out already used chests and Portrait chest
    available_chests = [chest_id for chest_id in valid_chests if chest_id not in used_chests and chest_id != PORTRAIT_CHEST_ID]
    
    if not available_chests:
        if verbose:
            print(f"No available chests in valid regions for {key_item}")
        return False, None, None, None
    
    # Choose a random chest
    shuffle_array(available_chests)
    chosen_chest_id = available_chests[0]
    
    return True, 'chest', chosen_chest_id, item_id

def place_starstones(chest_contents, shop_contents, used_chests, collected_items, verbose=False):
    """
    Place 5 Starstones needed to access Astarica
    
    Args:
        chest_contents (dict): Current chest contents mapping
        shop_contents (dict): Current shop contents mapping
        used_chests (set): Chests that have already been used
        collected_items (set): Currently collected items
        verbose (bool): Whether to print verbose output
        
    Returns:
        bool: True if successfully placed all 5 Starstones
    """
    starstone_id = ITEM_NAME_TO_ID.get('Starstone')
    if not starstone_id:
        if verbose:
            print(f"Missing ID for Starstone item")
        return False
    
    starstone_locations = 0
    
    # Get accessible areas and chests for late-game areas where Starstones should be placed
    late_area_chests = []
    for area in ['NEOTOKYO_SEWER', 'MU_REGION', 'GREAT_LAKES_CAVERN',]:
        if area in PROGRESSION_AREAS:
            late_area_chests.extend([chest_id for chest_id in PROGRESSION_AREAS[area]['contains'] 
                                     if chest_id not in used_chests and chest_id != PORTRAIT_CHEST_ID])
    
    # If we don't have enough late-game chests, use any accessible chests
    if len(late_area_chests) < 3:
        accessible_chests = get_accessible_chests(collected_items)
        late_area_chests.extend([chest_id for chest_id in accessible_chests 
                                if chest_id not in used_chests and chest_id not in late_area_chests and chest_id != PORTRAIT_CHEST_ID])
    
    # Shuffle the chest list
    shuffle_array(late_area_chests)
    
    # Place up to 3 Starstones in chests
    for i in range(min(3, len(late_area_chests))):
        chest_id = late_area_chests[i]
        chest_contents[chest_id] = starstone_id
        used_chests.add(chest_id)
        starstone_locations += 1
        
        if verbose:
            print(f"Placed Starstone #{starstone_locations} in chest {chest_id} ({get_chest_location_name(chest_id)})")
    
    # Get late-game shops for the remaining Starstones
    late_game_shops = []
    for shop_id in get_accessible_shops(collected_items):
        if shop_id.startswith('SHOP_FREEDOM') or shop_id.startswith('SHOP_SUNCOAST'):
            late_game_shops.append(shop_id)
    
    # If we don't have enough late-game shops, use any accessible shops
    if len(late_game_shops) < (5 - starstone_locations):
        accessible_shops = get_accessible_shops(collected_items)
        late_game_shops.extend([shop_id for shop_id in accessible_shops 
                               if shop_id not in late_game_shops])
    
    # Shuffle the shop list
    shuffle_array(late_game_shops)
    
    # Place remaining Starstones in shops
    for i in range(min(5 - starstone_locations, len(late_game_shops))):
        shop_id = late_game_shops[i]
        
        if shop_id not in shop_contents:
            shop_contents[shop_id] = []
        
        # Add Starstone to shop with a price
        price = 350 + random.randint(0, 200)
        shop_contents[shop_id].append({
            'itemId': starstone_id,
            'name': 'Starstone',
            'type': 'KEY_ITEM',
            'price': price,
            'bcdPrice': decimal_to_bcd(price),
            'limit': 1
        })
        
        starstone_locations += 1
        if verbose:
            shop_name = SHOP_ID_TO_NAME.get(shop_id, shop_id)
            print(f"Placed Starstone #{starstone_locations} in shop {shop_name} for {price} gems")
    
    # We still need more Starstones - use any remaining chests
    if starstone_locations < 5:
        remaining_chests = [chest_id for chest_id in CHEST_MAP.keys() if chest_id not in used_chests and chest_id != PORTRAIT_CHEST_ID]
        shuffle_array(remaining_chests)
        
        for i in range(min(5 - starstone_locations, len(remaining_chests))):
            chest_id = remaining_chests[i]
            chest_contents[chest_id] = starstone_id
            used_chests.add(chest_id)
            starstone_locations += 1
            
            if verbose:
                print(f"Placed Starstone #{starstone_locations} in chest {chest_id} ({get_chest_location_name(chest_id)}) (fallback)")
    
    # Check if we placed all 5
    if starstone_locations >= 5:
        if verbose:
            print(f"Successfully placed all 5 Starstones")
        return True
    else:
        if verbose:
            print(f"Warning: Could only place {starstone_locations}/5 Starstones")
        return False

def create_logical_placement(verbose=False):
    """
    Create a logical placement of items in chests that ensures the game is beatable
    
    Args:
        verbose (bool): Whether to print detailed logs
        
    Returns:
        dict: Map of chest IDs to item IDs or None if failed
    """
    if verbose:
        print("Creating logical placement...")
        print("NOTE: Portrait (chest 150) will remain in vanilla location")
    
    # Prepare our chest and shop placement maps
    chest_contents = {}
    shop_contents = {}
    used_chests = set()
    used_shop_slots = {}
    
    # Track placed items to ensure only one copy of each in the world
    placed_items = set()
    key_items_placed = set()
    collected_items = set()
    
    # Place key progression items
    # Start with those needed early in the game
    early_essentials = ['Crystal Thread', 'Giant Leaves', 'Ra Dewdrop', 'RocSpear', 'Sharp Claws']
    mid_essentials = ['Red Scarf', 'Protect Bell', 'Dog Whistle', 'Tower Key']
    
    # Place early essentials in very accessible areas
    early_chests = get_chests_for_regions(['UNDERWORLD_START', 'TREE_CAVE_ENTRANCE'])
    # Remove Portrait chest
    if PORTRAIT_CHEST_ID in early_chests:
        early_chests.remove(PORTRAIT_CHEST_ID)
    shuffle_array(early_chests)
    
    for i, key_item in enumerate(early_essentials):
        if i < len(early_chests):
            chest_id = early_chests[i]
            item_id = ITEM_NAME_TO_ID.get(key_item)
            
            if item_id:
                chest_contents[chest_id] = item_id
                used_chests.add(chest_id)
                key_items_placed.add(key_item)
                placed_items.add(item_id)
                collected_items.add(key_item)
                
                if verbose:
                    print(f"Placed {key_item} in chest {chest_id} ({get_chest_location_name(chest_id)})")
            else:
                if verbose:
                    print(f"Missing ID for item: {key_item}")
                return None
    
    # Now place Starstones
    if not place_starstones(chest_contents, shop_contents, used_chests, collected_items, verbose):
        if verbose:
            print("Failed to place all 5 Starstones")
        return None
    
    # Add special handling for mid-game essentials
    mid_game_chests = get_chests_for_regions(['SURFACE_INITIAL', 'GRECLIFF_ENTRANCE', 'GRECLIFF_MIDDLE', 'EKLEMATA_REGION'])
    mid_game_chests = [chest_id for chest_id in mid_game_chests if chest_id not in used_chests and chest_id != PORTRAIT_CHEST_ID]
    shuffle_array(mid_game_chests)
    
    for i, key_item in enumerate(mid_essentials):
        if i < len(mid_game_chests):
            chest_id = mid_game_chests[i]
            item_id = ITEM_NAME_TO_ID.get(key_item)
            
            if item_id:
                chest_contents[chest_id] = item_id
                used_chests.add(chest_id)
                key_items_placed.add(key_item)
                placed_items.add(item_id)
                collected_items.add(key_item)
                
                if verbose:
                    print(f"Placed {key_item} in chest {chest_id} ({get_chest_location_name(chest_id)})")
            else:
                if verbose:
                    print(f"Missing ID for item: {key_item}")
                return None
    
    # Fill remaining chests with regular items
    all_known_chest_ids = list(CHEST_MAP.keys())
    # Remove Portrait chest
    if PORTRAIT_CHEST_ID in all_known_chest_ids:
        all_known_chest_ids.remove(PORTRAIT_CHEST_ID)
    
    remaining_chests = [chest_id for chest_id in all_known_chest_ids if chest_id not in used_chests]
    
    # Get all non-key items for filling the rest
    from terranigma_randomizer.constants.items import ITEM_DATABASE
    regular_items = []
    for id_hex, item in ITEM_DATABASE.items():
        if item['name'] not in PROGRESSION_KEY_ITEMS:
            try:
                regular_items.append(int(id_hex, 16))
            except ValueError:
                # Skip if id_hex is not a valid hexadecimal
                continue
    
    # Ensure we have enough items
    if len(regular_items) == 0:
        if verbose:
            print("No regular items found!")
        return None
    
    shuffle_array(regular_items)
    
    # Fill remaining chests
    for i, chest_id in enumerate(remaining_chests):
        item_id = regular_items[i % len(regular_items)]
        chest_contents[chest_id] = item_id
    
    # Ensure Portrait stays in its vanilla location
    chest_contents[PORTRAIT_CHEST_ID] = PORTRAIT_ITEM_ID
    
    # Add Starstones5 to collected_items for validation
    collected_items.add('Starstones5')
    
    # Validate the placement
    if validate_game_progress(chest_contents, shop_contents, verbose):
        if verbose:
            print("Placement validated - game is beatable!")
            print(f"Portrait remains in chest {PORTRAIT_CHEST_ID}")
        return chest_contents
    else:
        if verbose:
            print("Placement validation failed - game is not beatable!")
        return None