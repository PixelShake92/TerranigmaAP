"""
Spoiler log generation functions for Terranigma Randomizer
"""

from terranigma_randomizer.constants.items import PROGRESSION_KEY_ITEMS, ITEM_DATABASE, get_item_name, ITEM_NAME_TO_ID, PORTRAIT_CHEST_ID, PORTRAIT_ITEM_ID

def generate_chest_spoiler_text(spoiler_log):
    """
    Generate a spoiler log text file for chest randomization
    
    Args:
        spoiler_log (list): Array of spoiler log entries
        
    Returns:
        str: Spoiler log text
    """
    text = 'Terranigma Chest Randomizer - Spoiler Log\n'
    text += '=========================================\n\n'
    
    # Add note about Portrait exclusion
    text += 'NOTE: Portrait remains in vanilla location (Stockholm House) due to entry bug\n\n'
    
    # Sort by map for easier reading
    spoiler_log.sort(key=lambda x: x['location'])
    
    # Organize by map
    map_groups = {}
    for entry in spoiler_log:
        map_name = entry['location'].split(' (')[0]
        if map_name not in map_groups:
            map_groups[map_name] = []
        map_groups[map_name].append(entry)
    
    text += 'Key Items Summary:\n'
    text += '================\n\n'
    
    for key_item in PROGRESSION_KEY_ITEMS:
        entry = next((e for e in spoiler_log if e['newItem'] == key_item), None)
        if entry:
            text += f"{key_item}: {entry['location']}\n"
        else:
            text += f"{key_item}: Not randomized\n"
    
    text += '\n\nChest Contents By Location:\n'
    text += '=========================\n\n'
    
    # Output by map for better organization
    for map_name in sorted(map_groups.keys()):
        text += f"{map_name}:\n"
        text += '-' * len(map_name) + '\n'
        
        for entry in map_groups[map_name]:
            position_match = entry['location'].split('(')
            position = f"({position_match[1]}" if len(position_match) > 1 else ''
            
            # Highlight key progression items
            item_text = entry['newItem']
            if item_text in PROGRESSION_KEY_ITEMS:
                item_text = f"{entry['newItem']} [KEY]"
            
            # Special marking for Portrait
            if entry['chestID'] == PORTRAIT_CHEST_ID:
                item_text += " [VANILLA - NOT RANDOMIZED]"
            
            text += f"  Chest ID {str(entry['chestID']).rjust(3)} {position}: {entry['originalItem']} → {item_text}\n"
            
            # Include note if present
            if 'note' in entry:
                text += f"    Note: {entry['note']}\n"
        
        text += '\n'
    
    return text

def generate_shop_spoiler_text(shops, seed):
    """
    Generate a spoiler log text file for shop randomization
    
    Args:
        shops (list): Array of randomized shop objects
        seed (int): Randomization seed
        
    Returns:
        str: Spoiler log text
    """
    text = 'Terranigma Shop Randomizer - Spoiler Log\n'
    text += '========================================\n\n'
    text += f'Seed: {seed}\n\n'
    
    # Group shops by area for better organization
    area_groups = {}
    for shop in shops:
        area = shop['location'].split(' - ')[0]
        if area not in area_groups:
            area_groups[area] = []
        area_groups[area].append(shop)
    
    # Check for key items in shops
    key_items_in_shops = []
    for shop in shops:
        for item in shop['items']:
            item_name = get_item_name(item['itemId'])
            if item_name in PROGRESSION_KEY_ITEMS:
                key_items_in_shops.append({
                    'shop': shop['location'],
                    'item': item_name,
                    'price': item['price']
                })
    
    # If there are key items in shops, highlight them at the beginning
    if key_items_in_shops:
        text += 'Key Items in Shops:\n'
        text += '=================\n\n'
        
        for entry in key_items_in_shops:
            text += f"{entry['item']}: {entry['shop']} - {entry['price']} gems\n"
        
        text += '\n'
    
    # Output shops grouped by area
    text += 'Shop Contents:\n'
    text += '=============\n\n'
    
    for area in sorted(area_groups.keys()):
        text += f"{area}:\n"
        text += '-' * len(area) + '\n'
        
        for shop in area_groups[area]:
            text += f"Shop ID {shop['id']}: {shop['location']}\n"
            
            for item in shop['items']:
                item_name = get_item_name(item['itemId'])
                limit_text = f" (Limit: {item['limit']})" if item['limit'] > 0 else ""
                
                # Highlight key items
                is_key_item = item_name in PROGRESSION_KEY_ITEMS
                item_text = f"{item_name} [KEY]" if is_key_item else item_name
                
                text += f"  {item_text} - {item['price']} gems{limit_text}\n"
            
            text += '\n'
    
    return text

def generate_enhanced_spoiler_text(result, seed):
    """
    Generate an enhanced spoiler log text file that includes shop information
    and unique item placement
    
    Args:
        result (dict): Randomization result with chest and shop spoiler logs
        seed (int): Randomization seed
        
    Returns:
        str: Spoiler log text
    """
    chest_spoiler_log = result['chest_spoiler_log']
    shop_spoiler_log = result['shop_spoiler_log']
    key_items_in_shops = result.get('key_items_in_shops', [])
    unique_items_in_shops = result.get('unique_items_in_shops', [])
    
    text = 'Terranigma Enhanced Randomizer - Spoiler Log\n'
    text += '=========================================\n\n'
    
    text += f'Seed: {seed}\n\n'
    
    # Add note about Portrait
    text += 'IMPORTANT: Portrait remains in vanilla location (Stockholm House, Chest 150)\n'
    text += 'due to a bug that prevents Storkolm entry if Portrait is in inventory.\n\n'
    
    # First, list all key items with their locations
    text += 'Key Item Locations Summary:\n'
    text += '=========================\n\n'
    
    # Find all possible Starstones
    starstone_chests = []
    starstone_shops = []
    
    # Look for Starstones in chests
    starstone_id = ITEM_NAME_TO_ID.get('Starstone')
    for entry in chest_spoiler_log:
        if entry['newItemId'] == starstone_id:
            starstone_chests.append(entry)
    
    # Look for Starstones in shops
    for shop in shop_spoiler_log:
        for item in shop['items']:
            if item['itemId'] == starstone_id:
                starstone_shops.append({
                    'shop_id': shop['id'],
                    'location': shop['location'],
                    'price': item['price'],
                    'item': 'Starstone'
                })
    
    # Compile comprehensive list of all Starstones
    all_starstones = []
    
    # Add chest Starstones
    for entry in starstone_chests:
        all_starstones.append({
            'type': 'chest',
            'location': entry['location']
        })
    
    # Add shop Starstones
    for entry in starstone_shops:
        all_starstones.append({
            'type': 'shop',
            'location': entry['location'],
            'price': entry['price']
        })
    
    # Also check key_items_in_shops for any missed Starstones
    for entry in key_items_in_shops:
        if entry['item'] == 'Starstone':
            # Check if this shop is already in our list
            if not any(s['type'] == 'shop' and s['location'] == entry['location'] for s in all_starstones):
                all_starstones.append({
                    'type': 'shop',
                    'location': entry['location'],
                    'price': entry['price']
                })
    
    # Now display all Starstones
    text += "Starstones (needed for Astarica):\n"
    
    # Use our comprehensive list of all found Starstones
    for i, starstone in enumerate(all_starstones):
        if i >= 5:  # Only need 5 Starstones
            break
            
        if starstone['type'] == 'chest':
            text += f"   - Starstone #{i+1}: In chest at {starstone['location']}\n"
        else:
            text += f"   - Starstone #{i+1}: In shop at {starstone['location']} - {starstone['price']} gems\n"
    
    # If we found fewer than 5, add placeholders to clearly show the issue
    for i in range(len(all_starstones), 5):
        text += f"   - Starstone #{i+1}: MISSING! This seed may be unbeatable!\n"
    
    text += "\n"
    
    # Organize key items by chest vs shop
    for key_item in PROGRESSION_KEY_ITEMS:
        # Skip Starstone if we already handled it
        if key_item == 'Starstone':
            continue
            
        # Check if in chest
        chest_entry = next((entry for entry in chest_spoiler_log if entry['newItem'] == key_item), None)
        
        # Check if in shop
        shop_entry = next((entry for entry in key_items_in_shops if entry['item'] == key_item), None)
        
        if chest_entry:
            text += f"{key_item}: Chest in {chest_entry['location']}\n"
        elif shop_entry:
            text += f"{key_item}: Shop in {shop_entry['location']} - {shop_entry['price']} gems"
            if shop_entry.get('limit', 0) > 0:
                text += f" (limit: {shop_entry['limit']})"
            text += '\n'
        else:
            text += f"{key_item}: Not found (potential error)\n"
    
    text += '\n'
    
    # Add a section for unique weapons and armor
    text += 'Unique Weapons and Armor Locations:\n'
    text += '===============================\n\n'
    
    # Find unique weapons in chests
    unique_weapons_in_chests = []
    for entry in chest_spoiler_log:
        id_hex = format(entry['newItemId'], '04X')
        item_info = ITEM_DATABASE.get(id_hex, {})
        if item_info.get('type') == 'weapon':
            unique_weapons_in_chests.append(entry)
    unique_weapons_in_chests.sort(key=lambda x: x['newItem'])
    
    # Find unique armor in chests
    unique_armor_in_chests = []
    for entry in chest_spoiler_log:
        id_hex = format(entry['newItemId'], '04X')
        item_info = ITEM_DATABASE.get(id_hex, {})
        if item_info.get('type') == 'armor':
            unique_armor_in_chests.append(entry)
    unique_armor_in_chests.sort(key=lambda x: x['newItem'])
    
    # Get unique weapons and armor from shops
    unique_weapons_in_shops = [entry for entry in unique_items_in_shops if entry['type'] == 'weapon']
    unique_weapons_in_shops.sort(key=lambda x: x['item'])
    
    unique_armor_in_shops = [entry for entry in unique_items_in_shops if entry['type'] == 'armor']
    unique_armor_in_shops.sort(key=lambda x: x['item'])
    
    # List weapons
    text += 'Weapons:\n'
    text += '--------\n'
    
    for entry in unique_weapons_in_chests:
        text += f"{entry['newItem']}: Chest in {entry['location']}\n"
    
    for entry in unique_weapons_in_shops:
        text += f"{entry['item']}: Shop in {entry['location']} - {entry['price']} gems"
        if entry.get('limit', 0) > 0:
            text += f" (limit: {entry['limit']})"
        text += '\n'
    
    text += '\n'
    
    # List armor
    text += 'Armor:\n'
    text += '------\n'
    
    for entry in unique_armor_in_chests:
        text += f"{entry['newItem']}: Chest in {entry['location']}\n"
    
    for entry in unique_armor_in_shops:
        text += f"{entry['item']}: Shop in {entry['location']} - {entry['price']} gems"
        if entry.get('limit', 0) > 0:
            text += f" (limit: {entry['limit']})"
        text += '\n'
    
    text += '\n'
    
    # Add detailed progression path guide
    text += 'Suggested Progression Path:\n'
    text += '=========================\n\n'
    
    text += '1. Start in the underworld\n'
    text += '2. Find the following early items (in chests and/or shops):\n'
    
    # Check where Giant Leaves, RocSpear, ElleCape, and Ra Dewdrop are
    critical_items = ['Giant Leaves', 'RocSpear', 'ElleCape', 'Ra Dewdrop']
    for item in critical_items:
        chest_entry = next((e for e in chest_spoiler_log if e['newItem'] == item), None)
        shop_entry = next((e for e in key_items_in_shops if e['item'] == item), None)
        
        if chest_entry:
            text += f"   - {item}: In chest at {chest_entry['location']}\n"
        elif shop_entry:
            text += f"   - {item}: In shop at {shop_entry['location']} - {shop_entry['price']} gems\n"
    
    text += '3. With Giant Leaves, gain access to the surface world\n'
    text += '4. With RocSpear, access Grecliff\n'
    text += '5. Find Sharp Claws to progress past Grecliff\n'
    
    sharp_claws_chest = next((e for e in chest_spoiler_log if e['newItem'] == 'Sharp Claws'), None)
    sharp_claws_shop = next((e for e in key_items_in_shops if e['item'] == 'Sharp Claws'), None)
    
    if sharp_claws_chest:
        text += f"   - Sharp Claws: In chest at {sharp_claws_chest['location']}\n"
    elif sharp_claws_shop:
        text += f"   - Sharp Claws: In shop at {sharp_claws_shop['location']} - {sharp_claws_shop['price']} gems\n"
    
    text += '6. Proceed to collect the remaining key items:\n'
    
    # List remaining key items
    remaining_items = [item for item in PROGRESSION_KEY_ITEMS 
                      if item not in critical_items and item != 'Sharp Claws' and item != 'Starstone']
    
    for item in remaining_items:
        chest_entry = next((e for e in chest_spoiler_log if e['newItem'] == item), None)
        shop_entry = next((e for e in key_items_in_shops if e['item'] == item), None)
        
        if chest_entry:
            text += f"   - {item}: In chest at {chest_entry['location']}\n"
        elif shop_entry:
            text += f"   - {item}: In shop at {shop_entry['location']} - {shop_entry['price']} gems\n"
    
    # Add a special section for Starstones
    text += '\n7. Collect all 5 Starstones to access Astarica:\n'
    
    # Use our comprehensive list of all found Starstones
    for i, starstone in enumerate(all_starstones):
        if i >= 5:  # Only need 5 Starstones
            break
            
        if starstone['type'] == 'chest':
            text += f"   - Starstone #{i+1}: In chest at {starstone['location']}\n"
        else:
            text += f"   - Starstone #{i+1}: In shop at {starstone['location']} - {starstone['price']} gems\n"
    
    # If we found fewer than 5, add placeholders
    for i in range(len(all_starstones), 5):
        text += f"   - Starstone #{i+1}: MISSING! This seed may be unbeatable!\n"
    
    text += '\n'
    
    return text