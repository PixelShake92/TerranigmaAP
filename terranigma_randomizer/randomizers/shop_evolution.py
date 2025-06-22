"""
Shop evolution handler for Terranigma Randomizer
Handles shops that share the same memory location but represent different stages
"""

from terranigma_randomizer.constants.items import PROGRESSION_KEY_ITEMS

# Shop evolution groups - shops that share the same physical location
# but represent different stages of town development
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
        {'id': 37, 'stage': 1, 'location': 'Suncoast- Right Merchant', 'fileOffset': 0x19D2A2},  # Shares with Freedom Inn!
        {'id': 38, 'stage': 2, 'location': 'Suncoast Merchant', 'fileOffset': 0x19D2A2},  # Also shares!
        {'id': 39, 'stage': 2, 'location': 'Suncoast - Merchant', 'fileOffset': 0x19D278}
    ],
    'NIRLAKE': [
        {'id': 15, 'stage': 1, 'location': 'Nirlake - House', 'fileOffset': 0x19D147},
        {'id': 16, 'stage': 2, 'location': '1st Ave. - Merchant', 'fileOffset': 0x19D15C},
        {'id': 42, 'stage': 3, 'location': 'Nirlake - Hotel - Room 2', 'fileOffset': 0x19D262}
    ]
}

# Create a mapping of file offsets to all shops that use them
SHARED_OFFSET_SHOPS = {}
for group_name, shops in SHOP_EVOLUTION_GROUPS.items():
    for shop in shops:
        offset = shop['fileOffset']
        if offset not in SHARED_OFFSET_SHOPS:
            SHARED_OFFSET_SHOPS[offset] = []
        SHARED_OFFSET_SHOPS[offset].append({
            'id': shop['id'],
            'location': shop['location'],
            'stage': shop['stage'],
            'group': group_name
        })

def get_evolution_group(shop_id):
    """
    Get the evolution group for a shop ID
    
    Args:
        shop_id (int): Shop ID
        
    Returns:
        tuple: (group_name, stage) or (None, None) if not in a group
    """
    for group_name, shops in SHOP_EVOLUTION_GROUPS.items():
        for shop in shops:
            if shop['id'] == shop_id:
                return group_name, shop['stage']
    return None, None

def get_shops_at_same_location(shop_id):
    """
    Get all shop IDs that share the same physical location
    
    Args:
        shop_id (int): Shop ID
        
    Returns:
        list: List of shop IDs at the same location
    """
    group_name, _ = get_evolution_group(shop_id)
    if group_name:
        return [shop['id'] for shop in SHOP_EVOLUTION_GROUPS[group_name]]
    return [shop_id]

def handle_shop_evolution_conflicts(shop_contents):
    """
    Handle conflicts when multiple shop stages share the same offset
    
    For shops that share offsets (different evolution stages), we need to
    decide which stage's contents to use. This function consolidates
    shop contents for shops that share offsets.
    
    Args:
        shop_contents (dict): Map of shop IDs to their contents
        
    Returns:
        dict: Adjusted shop contents with evolution conflicts resolved
    """
    adjusted_contents = {}
    processed_groups = set()
    
    for shop_id, contents in shop_contents.items():
        # Convert shop_id to int if it's a string
        try:
            shop_id = int(shop_id) if isinstance(shop_id, str) else shop_id
        except ValueError:
            adjusted_contents[shop_id] = contents
            continue
            
        group_name, stage = get_evolution_group(shop_id)
        
        if group_name and group_name not in processed_groups:
            # This shop is part of an evolution group
            processed_groups.add(group_name)
            
            # Get all shops in this group
            group_shops = SHOP_EVOLUTION_GROUPS[group_name]
            
            # Collect all items from all stages of this shop
            all_items = []
            all_shop_ids = []
            key_items_found = []
            
            for shop in group_shops:
                shop_id_to_check = shop['id']
                # Check both int and string versions of the ID
                if shop_id_to_check in shop_contents:
                    all_items.extend(shop_contents[shop_id_to_check])
                    all_shop_ids.append(shop_id_to_check)
                elif str(shop_id_to_check) in shop_contents:
                    all_items.extend(shop_contents[str(shop_id_to_check)])
                    all_shop_ids.append(shop_id_to_check)
                
                # Track key items
                for item in all_items:
                    if item.get('name') in PROGRESSION_KEY_ITEMS:
                        key_items_found.append(item['name'])
            
            # If we have items, distribute them across the stages
            if all_items:
                # Remove duplicates while preserving order
                unique_items = []
                seen_items = set()
                
                for item in all_items:
                    item_key = (item['itemId'], item['name'])
                    if item_key not in seen_items:
                        seen_items.add(item_key)
                        unique_items.append(item)
                
                # Assign the consolidated items to all stages
                # This ensures key items are available regardless of town state
                for shop_id_to_assign in all_shop_ids:
                    adjusted_contents[shop_id_to_assign] = unique_items
                    
                if key_items_found:
                    print(f"Consolidated {len(unique_items)} items across {group_name} shop stages: {all_shop_ids}")
                    print(f"  Key items preserved: {', '.join(key_items_found)}")
        
        elif group_name is None:
            # This shop is not part of an evolution group
            adjusted_contents[shop_id] = contents
    
    return adjusted_contents

def check_shared_offset_conflict(shop_id, file_offset):
    """
    Check if a shop shares its file offset with shops from different evolution groups
    
    Args:
        shop_id (int): Shop ID to check
        file_offset (int): File offset of the shop
        
    Returns:
        list: List of conflicting shop IDs from different groups
    """
    conflicts = []
    
    if file_offset in SHARED_OFFSET_SHOPS:
        shop_group, _ = get_evolution_group(shop_id)
        
        for other_shop in SHARED_OFFSET_SHOPS[file_offset]:
            if other_shop['id'] != shop_id and other_shop['group'] != shop_group:
                conflicts.append(other_shop)
    
    return conflicts