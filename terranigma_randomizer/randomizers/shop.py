"""
Shop randomization module for Terranigma Randomizer
"""

import random
from terranigma_randomizer.constants.shops import (
    KNOWN_SHOPS, SHOP_ID_TO_INDEX, decimal_to_bcd, bcd_to_decimal,
    SHOP_ITEM_ENTRY_SIZE, SHOP_ITEM_ID_OFFSET, 
    SHOP_PRICE_LOW_OFFSET, SHOP_PRICE_HIGH_OFFSET, SHOP_LIMIT_OFFSET
)
from terranigma_randomizer.constants.items import (
    ItemTypes, ITEM_DATABASE, get_item_name, get_item_info, PROGRESSION_KEY_ITEMS
)
from terranigma_randomizer.constants.progression import get_progression_tier, GAME_AREAS
from terranigma_randomizer.utils.logic import create_seeded_rng, shuffle_array
from terranigma_randomizer.constants.items import PORTRAIT_CHEST_ID, PORTRAIT_ITEM_ID

# Define shop regions based on game progression
SHOP_REGIONS = {
    'EARLY_GAME': [
        'Crysta Day', 'Crysta Night'  # Chapter 1 - First shops available
    ],
    'EARLY_SURFACE': [
        'Lumina (stage 1)', 'Lumina (stage 2/3)', 'Sanctuar (birds)', 'Sanctuar (pre-birds)', 'Safarium'
        # Chapter 2 - First surface shops
    ],
    'MID_GAME': [
        'Indus River - Ring Shop', 'Louran Shop', 'Lhase - Shop', 'Loire - Shop', 'Loire - Shop Weapons'
        # Chapter 3 early - Mid-game shops
    ],
    'LATE_MID_GAME': [
        'Freedom - Weapons', 'Freedom - Armor'
        # Chapter 3 mid - Freedom shops
    ],
    'LATE_GAME': [
        'Suncoast- Magishop - ', 'Suncoast - Merchant', 'Ring Shop'
        # Chapter 3 late/Chapter 4 - Later shops
    ]
}

# Create a mapping of shop locations to their regions
SHOP_LOCATION_TO_REGION = {}
for region, locations in SHOP_REGIONS.items():
    for location in locations:
        SHOP_LOCATION_TO_REGION[location] = region

# Key progression items that should be carefully placed
CRITICAL_KEY_ITEMS = [
    'Crystal Thread',  # Needed early for ElleCape
    'Sharp Claws',     # Needed for Grecliff
    'Giant Leaves',    # Needed for surface world
    'Ra Dewdrop',      # Needed for Ra Tree Boss
    'Sapphire'         # Needed for Bloody Mary
    'Topaz'            # Needed for Bloody Mary
    'Black Opal'       # Needed for Bloody Mary
    'Ruby'             # Needed for Bloody Mary
    'RocSpear',        # Needed for Grecliff
    'Red Scarf',       # Needed for Louran
    'Holy Seal',       # Needed for Louran
    'Tower Key',       # Needed for Dragoon Castle
    'Protect Bell',    # Needed for Norfest
    'Dog Whistle',     # Needed for Storkolm
    'Mushroom',        # Needed to put castle to sleep in Loire
    'Magic Anchor',    # Needed for Great Lakes Cave
    'Air Herb',        # Needed for underwater
]

# Define which regions can safely have which key items
KEY_ITEM_VALID_REGIONS = {
    'Crystal Thread': ['EARLY_GAME'],  # Must be available very early
    'Sharp Claws': ['EARLY_GAME', 'EARLY_SURFACE'],  # Needed after getting to surface
    'Giant Leaves': ['EARLY_GAME'],  # Needed to reach surface
    'Ra Dewdrop': ['EARLY_GAME'],  # Needed for tree boss
    'RocSpear': ['EARLY_GAME', 'EARLY_SURFACE'],  # Needed for Grecliff
    'Red Scarf': ['EARLY_GAME', 'EARLY_SURFACE', 'MID_GAME'],  # Needed for Louran
    'Tower Key': ['MID_GAME', 'LATE_MID_GAME'],  # Later game
    'Protect Bell': ['EARLY_SURFACE', 'MID_GAME'],  # Mid-game
    'Holy Seal': ['EARLY_GAME', 'EARLY_SURFACE', 'MID_GAME'],  # Needed before endgame
    'Mushroom': ['EARLY_SURFACE', 'MID_GAME'],  # Needed to put castle to sleep in Loire
    'Dog Whistle': ['MID_GAME'],  # Mid-game
    'Magic Anchor': ['MID_GAME', 'LATE_MID_GAME'],  # Mid-to-late game
    'Air Herb': ['MID_GAME', 'LATE_MID_GAME'],  # Mid-to-late game
    'Engagement Ring': ['MID_GAME', 'LATE_MID_GAME'],  # Mid-to-late game
    'Transceiver': ['LATE_MID_GAME', 'LATE_GAME'],  # Late game
    'Starstone': ['LATE_MID_GAME', 'LATE_GAME'],  # Late game
    'Sewer Key': ['MID_GAME', 'LATE_MID_GAME'],  # Mid-to-late game
    'Speed Shoes': ['MID_GAME', 'LATE_MID_GAME'],  # Mid-to-late game
    'Time Bomb': ['LATE_GAME'],  # End game
}

def is_magirock_shop(shop):
    """
    Determine if a shop uses Magirocks instead of gems
    
    Args:
        shop (dict): Shop object
        
    Returns:
        bool: True if this is a Magirock shop
    """
    # Check shop location name for Magirock shops
    location = shop.get('location', '').lower()
    
    # Known Magirock shop IDs (based on game data)
    # These are the actual magic/ring shops that use Magirocks
    magirock_shop_ids = [43, 44, 45, 46, 48, 49]  # Add more if needed
    
    # Check by shop ID first (more reliable)
    if shop.get('id') in magirock_shop_ids:
        return True
    
    # Fallback to name patterns
    magirock_patterns = ['magic shop', 'magishop', 'ring shop']
    
    # Special case - Indus River sells items for gems, not magirocks
    if 'indus river' in location:
        return False
    
    return any(pattern in location for pattern in magirock_patterns)

def get_shop_region(shop_location):
    """
    Get the progression region for a shop
    
    Args:
        shop_location (str): Shop location name
        
    Returns:
        str: Region identifier
    """
    return SHOP_LOCATION_TO_REGION.get(shop_location, 'MID_GAME')  # Default to MID_GAME if not found

def read_shops_from_rom(rom_data):
    """
    Read shop data using our known shop database
    
    Args:
        rom_data (bytearray): ROM buffer
        
    Returns:
        list: Array of shop objects with current data
    """
    print('Reading shop data from ROM using known addresses...')
    
    # Create a deep copy of the known shops array
    import copy
    shops = copy.deepcopy(KNOWN_SHOPS)
    
    # For each shop, read the current data from ROM
    for i, shop in enumerate(shops):
        file_offset = shop['fileOffset']
        
        # Skip if the offset is invalid or beyond the buffer
        if not file_offset or file_offset >= len(rom_data):
            print(f"Warning: Invalid file offset {file_offset} for shop {shop['id']}")
            continue
        
        # Read items up to the end marker or maximum count
        items = []
        sale_id = 0
        
        # Use a higher limit to ensure we read all items
        max_items = 15  # Maximum possible items in a shop
        
        while sale_id < max_items:
            item_offset = file_offset + SHOP_ITEM_ENTRY_SIZE * sale_id
            
            # Check if we're past the end of the buffer
            if item_offset >= len(rom_data):
                break
            
            # Read item ID
            item_id = rom_data[item_offset + SHOP_ITEM_ID_OFFSET]
            
            # Check if we've reached the end marker (0xFF)
            if item_id == 0xFF:
                break  # End of shop items
            
            # Read price (BCD format)
            bcd_price = rom_data[item_offset + SHOP_PRICE_LOW_OFFSET] | (rom_data[item_offset + SHOP_PRICE_HIGH_OFFSET] << 8)
            price = bcd_to_decimal(bcd_price)
            
            # Read purchase limit
            limit = rom_data[item_offset + SHOP_LIMIT_OFFSET]
            
            # Get item information
            item_info = get_item_info(item_id)
            
            items.append({
                'itemId': item_id,
                'name': item_info.get('name', 'Unknown'),
                'type': item_info.get('type', 'Unknown'),
                'price': price,
                'bcdPrice': bcd_price,
                'limit': limit
            })
            
            sale_id += 1
        
        # Update the shop with the items read from ROM
        shop['items'] = items
        
        # Add region information to each shop
        shop['region'] = get_shop_region(shop['location'])
    
    return shops

def write_shops_to_rom(rom_data, shops):
    """
    Write shops to ROM
    
    Args:
        rom_data (bytearray): ROM buffer
        shops (list): Array of shop objects
        
    Returns:
        bytearray: Modified ROM buffer
    """
    new_rom_data = bytearray(rom_data)
    
    print(f"Writing {len(shops)} shops to ROM...")
    
    # Process each shop
    for shop in shops:
        # Find the shop template in our known shops array
        shop_index = SHOP_ID_TO_INDEX.get(shop['id'])
        if shop_index is None:
            print(f"Warning: Shop ID {shop['id']} (type: {type(shop['id'])}) not found in known shops - skipping")
            continue
        
        known_shop = KNOWN_SHOPS[shop_index]
        file_offset = known_shop['fileOffset']
        
        print(f"Shop ID {shop['id']} ({shop.get('location', 'Unknown')}): Writing to offset {hex(file_offset)}")
        print(f"  Items: {len(shop['items'])}")
        
        # Safety check - validate file offset is within buffer boundaries
        if file_offset + (len(shop['items']) * SHOP_ITEM_ENTRY_SIZE) + 1 > len(new_rom_data):
            print(f"Warning: File offset {hex(file_offset)} for shop {shop['id']} is beyond buffer bounds - skipping")
            continue
        
        # Handle length limit - use the actual number of items we want to write
        max_items = min(len(shop['items']), 15)  # Hard limit of 15 items per shop
        
        # Write each item
        for i in range(max_items):
            item = shop['items'][i]
            item_offset = file_offset + (SHOP_ITEM_ENTRY_SIZE * i)
            
            try:
                # Write item ID
                new_rom_data[item_offset + SHOP_ITEM_ID_OFFSET] = item['itemId'] & 0xFF
                
                # Get BCD price and validate it
                valid_bcd_price = item.get('bcdPrice', decimal_to_bcd(item['price']))
                
                # Write BCD price
                price_low = valid_bcd_price & 0xFF
                price_high = (valid_bcd_price >> 8) & 0xFF
                
                new_rom_data[item_offset + SHOP_PRICE_LOW_OFFSET] = price_low
                new_rom_data[item_offset + SHOP_PRICE_HIGH_OFFSET] = price_high
                
                # Write purchase limit
                new_rom_data[item_offset + SHOP_LIMIT_OFFSET] = item['limit'] & 0xFF
                
                # Debug output for key items
                if item['name'] == 'Starstone' or item['name'] in PROGRESSION_KEY_ITEMS:
                    print(f"    Item {i}: {item['name']} (ID: {item['itemId']}, Price: {item['price']}, BCD: 0x{valid_bcd_price:04X}, Limit: {item['limit']})")
                else:
                    print(f"    Item {i}: {item['name']} (ID: {item['itemId']}, Price: {item['price']}, Limit: {item['limit']})")
            except Exception as e:
                print(f"Error writing item {item['name']} to shop {shop['id']}: {e}")
        
        # Write end marker (0xFF) only after all items
        end_offset = file_offset + (SHOP_ITEM_ENTRY_SIZE * max_items)
        new_rom_data[end_offset] = 0xFF
        print(f"  Wrote {max_items} items to shop {shop['id']}")
    
    # Verify the shops were written correctly
    print("\nVerifying shops were written correctly...")
    verification_shops = []
    try:
        # Don't print verbose logs during verification
        temp_print = print
        def silent_print(*args, **kwargs):
            pass
        globals()['print'] = silent_print
        
        verification_shops = read_shops_from_rom(new_rom_data)
        
        # Restore print function
        globals()['print'] = temp_print
        
        for shop in verification_shops:
            # Check if the shop has key items
            key_items = [item for item in shop['items'] if item['name'] in PROGRESSION_KEY_ITEMS]
            if key_items:
                print(f"  Verified shop {shop['id']} ({shop['location']}) has {len(key_items)} key items:")
                for item in key_items:
                    print(f"    - {item['name']} (ID: {item['itemId']}, Price: {item['price']})")
    except Exception as e:
        # Restore print function if an error occurred
        globals()['print'] = temp_print
        print(f"Error during verification: {e}")
    
    return new_rom_data

def calculate_item_price(item, tier, rng, options, is_magirock=False):
    """
    Calculate a price for an item based on its type, power, and game tier
    
    Args:
        item (dict): Item object with type and power properties
        tier (int): Game progression tier
        rng (function): Random number generator function
        options (dict): Options for price calculation
        is_magirock (bool): Whether this is for a Magirock shop
        
    Returns:
        int: Calculated price
    """
    base_price = 0
    
    # Special handling for Magirock shops
    if is_magirock:
        # Magirock prices should be very low (1-5 range) since there are only 100 total
        if item['type'] == ItemTypes.RING:
            base_price = 1  # Rings always cost 1-2 Magirocks
        elif item['type'] == ItemTypes.KEY_ITEM:
            # Key items in Magirock shops cost 3-5 Magirocks
            base_price = 3 + (tier // 2)  # 3-5 range based on tier
        else:
            # Other items cost 2-3 Magirocks
            base_price = 2
            
        # Apply very small variation to keep prices reasonable
        if options.get('randomize_prices', True) and options.get('price_variation', 0) > 0:
            # For Magirocks, only add 0-1 extra
            if item['type'] == ItemTypes.RING:
                base_price = min(2, base_price + (1 if rng() > 0.5 else 0))
            elif item['type'] == ItemTypes.KEY_ITEM:
                base_price = min(5, base_price + (1 if rng() > 0.7 else 0))
            else:
                base_price = min(3, base_price + (1 if rng() > 0.5 else 0))
        
        return base_price
    
    # Original gem-based pricing logic
    # Calculate base price by item type and power
    if item['type'] == ItemTypes.WEAPON or item['type'] == ItemTypes.ARMOR:
        # Scale by power and tier
        base_price = (item.get('power', 1) * 100) * (tier + 1)
    elif item['type'] == ItemTypes.CONSUMABLE:
        # Standard consumable pricing
        name = item['name']
        if name == 'S.Bulb':
            base_price = 10
        elif name == 'M.Bulb':
            base_price = 25
        elif name == 'L.Bulb':
            base_price = 70
        elif name == 'P. Cure':
            base_price = 13
        elif name == 'Stardew':
            base_price = 30
        elif name == 'Serum':
            base_price = 45
        elif name == 'H.Water':
            base_price = 90
        elif name == 'STR Potion':
            base_price = 110
        elif name == 'DEF Potion':
            base_price = 110
        elif name == 'Luck Potion':
            base_price = 130
        elif name == 'Life Potion':
            base_price = 150
        else:
            base_price = (item.get('power', 1)) * 20
    elif item['type'] == ItemTypes.RING:
        base_price = 10 + (tier * 5)
    elif item['type'] == ItemTypes.GEMS:
        # Gems are worth their value
        base_price = item.get('value', 10)
    elif item['type'] == ItemTypes.KEY_ITEM:
        # Key items are expensive
        base_price = 300 + (tier * 100)
    else:
        # Default pricing for other items
        base_price = 50 * (tier + 1)
    
    # Apply price variation if enabled
    if options.get('randomize_prices', True) and options.get('price_variation', 0) > 0:
        variation = 1 + ((rng() * options['price_variation'] * 2) - options['price_variation']) / 100
        base_price = max(1, int(base_price * variation))
    
    return base_price

def determine_item_limit(item, rng, options):
    """
    Determine purchase limit for an item
    
    Args:
        item (dict): Item object
        rng (function): Random number generator function
        options (dict): Options for limit determination
        
    Returns:
        int: Purchase limit (0 for no limit)
    """
    # Key items, weapons, and armor are typically limited to 1 purchase
    if item['type'] == ItemTypes.KEY_ITEM or item['type'] == ItemTypes.WEAPON or item['type'] == ItemTypes.ARMOR:
        return 1
    
    # Rings are sometimes limited
    if item['type'] == ItemTypes.RING:
        return 1 if rng() < 0.3 else 0
    
    # Consumables and other items usually have no limit
    return 0

def validate_shop_prices(shops):
    """
    Validate and fix shop prices
    
    Args:
        shops (list): Array of shop objects
    """
    for shop in shops:
        for i, item in enumerate(shop['items']):
            # Check if this is a Magirock shop
            if is_magirock_shop(shop):
                # Magirock shops have much lower price limits
                if item['price'] > 99:
                    item['price'] = 99
                    item['bcdPrice'] = decimal_to_bcd(99)
            else:
                # Regular gem shops
                if item['price'] > 9999:
                    item['price'] = 9999
                    item['bcdPrice'] = decimal_to_bcd(9999)
            
            # Ensure price isn't too low
            if item['price'] < 1:
                item['price'] = 1
                item['bcdPrice'] = decimal_to_bcd(1)
            
            # Verify BCD conversion is correct
            item['bcdPrice'] = decimal_to_bcd(item['price'])

def validate_shop_item_counts(shops):
    """
    Validate and fix shop item counts
    
    Args:
        shops (list): Array of shop objects
    """
    # Find matching shop in known shops to determine original count
    for shop in shops:
        shop_index = SHOP_ID_TO_INDEX.get(shop['id'])
        
        if shop_index is not None:
            original_shop = KNOWN_SHOPS[shop_index]
            # Don't limit to original count - allow up to 15 items
            max_items = min(15, len(shop['items']))
            
            # Trim if necessary
            if len(shop['items']) > max_items:
                print(f"Shop {shop['id']} ({shop['location']}) has too many items. Trimming from {len(shop['items'])} to {max_items}.")
                shop['items'] = shop['items'][:max_items]

def distribute_key_items_to_shops(shops, key_items_to_place, rng, options):
    """
    Distribute key items to appropriate shops based on game progression
    
    Args:
        shops (list): Array of shop objects
        key_items_to_place (list): List of key items to be placed
        rng (function): Random number generator
        options (dict): Randomization options
        
    Returns:
        dict: Map of shop IDs to key items placed in them
    """
    # Group shops by region
    shops_by_region = {}
    for shop in shops:
        region = shop['region']
        if region not in shops_by_region:
            shops_by_region[region] = []
        shops_by_region[region].append(shop)
    
    # For each key item, find appropriate shops by region
    key_item_placements = {}
    
    for key_item in key_items_to_place:
        # Get valid regions for this key item
        valid_regions = KEY_ITEM_VALID_REGIONS.get(key_item, ['MID_GAME'])
        
        # Collect all eligible shops
        eligible_shops = []
        for region in valid_regions:
            if region in shops_by_region:
                # Filter out Magirock shops unless we have no other choice
                regional_shops = shops_by_region[region]
                gem_shops = [s for s in regional_shops if not is_magirock_shop(s)]
                
                # Use gem shops if available, otherwise fall back to all shops
                if gem_shops:
                    eligible_shops.extend(gem_shops)
                else:
                    # If forced to use Magirock shops, only use them for affordable items
                    if key_item not in ['Tower Key', 'Magic Anchor', 'Starstone']:
                        eligible_shops.extend(regional_shops)
                    else:
                        print(f"Warning: Cannot place {key_item} in Magirock shops (too expensive)")
        
        # If still no eligible shops, use MID_GAME gem shops as fallback
        if not eligible_shops and 'MID_GAME' in shops_by_region:
            gem_shops = [s for s in shops_by_region['MID_GAME'] if not is_magirock_shop(s)]
            if gem_shops:
                eligible_shops = gem_shops
                print(f"Warning: No eligible shops found for {key_item}, falling back to MID_GAME gem shops")
        
        # If still no eligible shops, use any gem shop
        if not eligible_shops:
            all_gem_shops = [s for s in shops if not is_magirock_shop(s)]
            if all_gem_shops:
                eligible_shops = all_gem_shops
                print(f"Warning: No MID_GAME shops found for {key_item}, using any available gem shop")
        
        # If we have eligible shops, randomly select one
        if eligible_shops:
            shuffle_array(eligible_shops)
            chosen_shop = eligible_shops[0]
            
            # Add key item to the shop's placements
            shop_id = chosen_shop['id']
            if shop_id not in key_item_placements:
                key_item_placements[shop_id] = []
            
            key_item_placements[shop_id].append(key_item)
            
            # Print placement info
            shop_type = "Magirock" if is_magirock_shop(chosen_shop) else "Gem"
            print(f"Placed key item {key_item} in {chosen_shop['location']} shop (region: {chosen_shop['region']}, type: {shop_type})")
            
            # Remove the shop from eligible shops to avoid overloading a single shop
            for region in shops_by_region:
                shops_by_region[region] = [s for s in shops_by_region[region] if s['id'] != shop_id]
        else:
            print(f"ERROR: Could not place key item {key_item} - no eligible shops available")
    
    return key_item_placements

def randomize_shop_with_key_items(shop, key_items, rng, options):
    """
    Randomize a shop, ensuring it contains specified key items
    
    Args:
        shop (dict): Shop data
        key_items (list): Key items to include in this shop
        rng (function): Random number generator
        options (dict): Randomization options
        
    Returns:
        dict: Randomized shop
    """
    import copy
    randomized_shop = copy.deepcopy(shop)
    tier = get_progression_tier(shop['location'])
    region = shop['region']
    shop_uses_magirocks = is_magirock_shop(shop)
    
    # Filter out any invalid items with ID #255
    randomized_shop['items'] = [item for item in randomized_shop['items'] if item['itemId'] != 255]
    
    # Get the original item count from KNOWN_SHOPS
    shop_index = SHOP_ID_TO_INDEX.get(shop['id'])
    original_item_count = len(KNOWN_SHOPS[shop_index]['items']) if shop_index is not None else 5
    
    # Start with key items
    new_items = []
    for key_item in key_items:
        item_id = None
        item_info = None
        
        # Find item ID for this key item
        for id_hex, item in ITEM_DATABASE.items():
            if item['name'] == key_item:
                item_id = int(id_hex, 16)
                item_info = item
                break
        
        if item_id is not None:
            # Calculate price based on shop type
            if shop_uses_magirocks:
                # Magirock pricing for key items (3-5 Magirocks)
                base_price = 4  # Default to 4 Magirocks for key items
                
                # Add small variation (3-5 range)
                price = base_price + (1 if rng() > 0.7 else -1 if rng() < 0.3 else 0)
                price = max(3, min(5, price))  # Ensure 3-5 range
            else:
                # Regular gem pricing
                region_tier_bonus = {'EARLY_GAME': 0, 'EARLY_SURFACE': 1, 'MID_GAME': 2, 'LATE_MID_GAME': 3, 'LATE_GAME': 4}
                tier_bonus = region_tier_bonus.get(region, 0)
                base_price = 400 + (tier_bonus * 200)
                
                # Add variation
                if options.get('randomize_prices', True) and options.get('price_variation', 0) > 0:
                    variation = 1 + ((rng() * options['price_variation'] * 2) - options['price_variation']) / 100
                    price = max(1, int(base_price * variation))
                else:
                    price = base_price
            
            new_items.append({
                'itemId': item_id,
                'name': key_item,
                'type': ItemTypes.KEY_ITEM,
                'price': price,
                'bcdPrice': decimal_to_bcd(price),
                'limit': 1  # Key items are limited to 1 purchase
            })
            
            currency = "Magirocks" if shop_uses_magirocks else "gems"
            print(f"Added key item {key_item} to shop {shop['id']} ({shop['location']}) for {price} {currency}")
    
    # Determine number of items for this shop based on options
    items_per_shop = options.get('items_per_shop', 'normal')
    if items_per_shop == 'more':
        target_item_count = min(15, max(original_item_count + 3, 8 + int(rng() * 4)))  # More items than original
    elif items_per_shop == 'fewer':
        target_item_count = max(len(new_items) + 1, min(original_item_count - 1, 3 + int(rng() * 3)))  # Fewer items
    else:  # normal
        target_item_count = max(original_item_count, len(new_items))  # At least original count
    
    # Now randomize remaining items
    # Create an array of items to potentially add to shops
    all_possible_items = []
    
    # Add weapons (not for Magirock shops)
    if not shop_uses_magirocks:
        weapons = []
        for id_hex, item in ITEM_DATABASE.items():
            if item['type'] == ItemTypes.WEAPON:
                weapons.append({'id': id_hex, **item})
        all_possible_items.extend(weapons)
    
    # Add armor (not for Magirock shops)
    if not shop_uses_magirocks:
        armor = []
        for id_hex, item in ITEM_DATABASE.items():
            if item['type'] == ItemTypes.ARMOR:
                armor.append({'id': id_hex, **item})
        all_possible_items.extend(armor)
    
    # Add consumables (not typical for Magirock shops)
    if not shop_uses_magirocks:
        consumables = []
        for id_hex, item in ITEM_DATABASE.items():
            if item['type'] == ItemTypes.CONSUMABLE:
                consumables.append({'id': id_hex, **item})
        all_possible_items.extend(consumables)
    
    # Add rings (primary items for Magirock shops)
    rings = []
    for id_hex, item in ITEM_DATABASE.items():
        if item['type'] == ItemTypes.RING:
            rings.append({'id': id_hex, **item})
    all_possible_items.extend(rings)
    
    # If we want to add other items like accessories
    if options.get('include_accessories', False) and not shop_uses_magirocks:
        accessories = []
        for id_hex, item in ITEM_DATABASE.items():
            if item['type'] == ItemTypes.ACCESSORY:
                accessories.append({'id': id_hex, **item})
        all_possible_items.extend(accessories)
    
    # Filter out any key items that we don't want in shops unless specifically enabled
    if not options.get('include_key_items', False):
        all_possible_items = [
            item for item in all_possible_items 
            if item['type'] != ItemTypes.KEY_ITEM or 
            (options.get('special_items') and item['name'] in options['special_items'])
        ]
    
    # Filter out key items that we've already placed
    all_possible_items = [
        item for item in all_possible_items 
        if item['type'] != ItemTypes.KEY_ITEM or item['name'] not in key_items
    ]
    
    # Keep some original shop characteristics
    shop_type_count = {
        ItemTypes.WEAPON: 0,
        ItemTypes.ARMOR: 0,
        ItemTypes.CONSUMABLE: 0, 
        ItemTypes.RING: 0,
        ItemTypes.ACCESSORY: 0
    }
    
    # Count original types
    for item in shop['items']:
        if item['type'] in shop_type_count:
            shop_type_count[item['type']] += 1
    
    # Special handling for Magirock shops - they should primarily have rings
    if shop_uses_magirocks:
        shop_type_count[ItemTypes.RING] = max(shop_type_count[ItemTypes.RING], 5)
        shop_type_count[ItemTypes.WEAPON] = 0
        shop_type_count[ItemTypes.ARMOR] = 0
        shop_type_count[ItemTypes.CONSUMABLE] = 0
    
    # Special case for Ring Shops - make sure we've added rings
    if shop_uses_magirocks and any(item['type'] == ItemTypes.RING for item in all_possible_items):
        ring_items = [item for item in all_possible_items if item['type'] == ItemTypes.RING]
        
        # Add rings to fill the shop
        while len(new_items) < target_item_count and ring_items:
            random_index = int(rng() * len(ring_items))
            selected_ring = ring_items[random_index]
            
            ring_id = int(selected_ring['id'], 16)
            price = calculate_item_price(selected_ring, tier, rng, options, shop_uses_magirocks)
            
            new_items.append({
                'itemId': ring_id,
                'name': selected_ring['name'],
                'type': selected_ring['type'],
                'price': price,
                'bcdPrice': decimal_to_bcd(price),
                'limit': 0  # Rings typically don't have limits
            })
            
            # Remove ring to avoid duplicates
            ring_items.pop(random_index)
            all_possible_items = [item for item in all_possible_items if item['id'] != selected_ring['id']]
    
    # For non-Magirock shops, add variety of items
    if not shop_uses_magirocks:
        # Add at least one item of each type that was in the original shop
        for item_type, count in shop_type_count.items():
            if count > 0 and item_type != ItemTypes.RING:  # Skip rings for non-Magirock shops
                # Find eligible items of this type
                eligible_items = [
                    item for item in all_possible_items 
                    if item['type'] == item_type and 
                    (item_type not in [ItemTypes.WEAPON, ItemTypes.ARMOR, ItemTypes.RING] or 
                     not options.get('scale_equipment', True) or 
                     (item.get('power', 0) >= max(1, tier * 2) and 
                      item.get('power', 0) <= min(12, tier * 2 + 5)))
                ]
                
                if eligible_items:
                    # Add 1-3 items of this type
                    type_count = min(max(1, int(count * 0.7)), 3)
                    
                    for _ in range(type_count):
                        if not eligible_items or len(new_items) >= target_item_count:
                            break
                        
                        random_index = int(rng() * len(eligible_items))
                        selected_item = eligible_items[random_index]
                        
                        # Create item entry
                        item_id = int(selected_item['id'], 16)
                        price = calculate_item_price(selected_item, tier, rng, options, shop_uses_magirocks)
                        
                        new_items.append({
                            'itemId': item_id,
                            'name': selected_item['name'],
                            'type': selected_item['type'],
                            'price': price,
                            'bcdPrice': decimal_to_bcd(price),
                            'limit': determine_item_limit(selected_item, rng, options)
                        })
                        
                        # Remove the item to avoid duplicates
                        eligible_items.pop(random_index)
                        all_possible_items = [item for item in all_possible_items if item['id'] != selected_item['id']]
    
    # Fill remaining slots with appropriate items
    while len(new_items) < target_item_count and all_possible_items:
        # For Magirock shops, heavily favor rings
        if shop_uses_magirocks:
            ring_items = [item for item in all_possible_items if item['type'] == ItemTypes.RING]
            if ring_items:
                tier_items = ring_items
            else:
                break  # No more rings available
        else:
            # For regular shops, use variety
            tier_items = all_possible_items
        
        if not tier_items:
            break
        
        # Select a random item
        random_index = int(rng() * len(tier_items))
        selected_item = tier_items[random_index]
        
        # Skip if we already have this item
        if any(item['name'] == selected_item['name'] for item in new_items):
            # Remove to avoid checking again
            all_possible_items = [item for item in all_possible_items if item['id'] != selected_item['id']]
            continue
        
        # Create item entry
        item_id = int(selected_item['id'], 16)
        price = calculate_item_price(selected_item, tier, rng, options, shop_uses_magirocks)
        
        new_items.append({
            'itemId': item_id,
            'name': selected_item['name'],
            'type': selected_item['type'],
            'price': price,
            'bcdPrice': decimal_to_bcd(price),
            'limit': determine_item_limit(selected_item, rng, options)
        })
        
        # Remove the item to avoid duplicates
        all_possible_items = [item for item in all_possible_items if item['id'] != selected_item['id']]
    
    # Final check - make sure all shops have at least one item
    if not new_items:
        if shop_uses_magirocks:
            # Add a basic ring
            basic_ring = {
                'itemId': 0x01,  # FireRing
                'name': 'FireRing',
                'type': ItemTypes.RING,
                'price': 10,
                'bcdPrice': decimal_to_bcd(10),
                'limit': 0
            }
        else:
            # Add a basic consumable
            basic_ring = {
                'itemId': 0x10,  # S.Bulb
                'name': 'S.Bulb',
                'type': ItemTypes.CONSUMABLE,
                'price': 10,
                'bcdPrice': decimal_to_bcd(10),
                'limit': 0
            }
        
        new_items.append(basic_ring)
        print(f"Shop {shop['id']} ({shop['location']}) had no items, added a basic item")
    
    randomized_shop['items'] = new_items
    
    return randomized_shop

def randomize_shops(rom_data, options):
    """
    Main shop randomizer function with improved reliability and region logic
    
    Args:
        rom_data (bytearray): ROM buffer
        options (dict): Randomization options
        
    Returns:
        dict: Modified ROM buffer and randomized shops
    """
    print('\nRandomizing shops with region logic...')
    
    # Read shop data using our known addresses
    shops = read_shops_from_rom(rom_data)
    print(f"Using {len(shops)} shops from the known shops database.")
    
    # Check regions
    for shop in shops:
        shop_type = "Magirock" if is_magirock_shop(shop) else "Gem"
        print(f"Shop {shop['id']} ({shop['location']}) - Region: {shop['region']}, Type: {shop_type}")
    
    # Create RNG with seed
    rng = create_seeded_rng(options.get('seed', random.randint(0, 999999)))
    
    # Determine which key items to place in shops
    key_items_for_shops = []
    if options.get('integrate_shop_logic', True):
        # Percentage of key items to place in shops (25-35%)
        key_item_percent = 0.3 + (rng() * 0.1 - 0.05)  # 25-35%
        num_key_items = int(len(CRITICAL_KEY_ITEMS) * key_item_percent)
        num_key_items = max(2, min(num_key_items, 5))  # At least 2, at most 5
        
        # Choose which key items to place in shops
        shuffle_array(CRITICAL_KEY_ITEMS)
        key_items_for_shops = CRITICAL_KEY_ITEMS[:num_key_items]
        
        print(f"\nPlacing {num_key_items} key items in shops:")
        for item in key_items_for_shops:
            print(f"- {item}")
    
    # Distribute key items to shops based on region logic
    key_item_placements = distribute_key_items_to_shops(shops, key_items_for_shops, rng, options)
    
    # Randomize each shop, ensuring key items are included
    randomized_shops = []
    for shop in shops:
        # Get key items for this shop
        shop_key_items = key_item_placements.get(shop['id'], [])
        
        # Randomize the shop with key items
        randomized_shop = randomize_shop_with_key_items(shop, shop_key_items, rng, options)
        randomized_shops.append(randomized_shop)
    
    # Validate prices
    validate_shop_prices(randomized_shops)
    
    # Validate item counts
    validate_shop_item_counts(randomized_shops)
    
    # Write changes back to the ROM
    modified_rom = write_shops_to_rom(rom_data, randomized_shops)
    
    # Create a list of key items in shops for the spoiler log
    key_items_in_shops = []
    for shop in randomized_shops:
        for item in shop['items']:
            if item['name'] in PROGRESSION_KEY_ITEMS:
                currency = "Magirocks" if is_magirock_shop(shop) else "gems"
                key_items_in_shops.append({
                    'item': item['name'],
                    'shop': shop['location'],
                    'region': shop['region'],
                    'price': item['price'],
                    'currency': currency
                })
    
    if key_items_in_shops:
        print("\nKey items placed in shops:")
        for entry in key_items_in_shops:
            print(f"- {entry['item']} in {entry['shop']} ({entry['region']}) - {entry['price']} {entry['currency']}")
    
    return {
        'rom': modified_rom,
        'shops': randomized_shops,
        'key_items_in_shops': key_items_in_shops
    }