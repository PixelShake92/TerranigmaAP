"""
Chest randomization module for Terranigma Randomizer
"""

import random
from terranigma_randomizer.constants.chests import CHEST_MAP, KNOWN_CHESTS
from terranigma_randomizer.constants.items import get_item_name, PROGRESSION_KEY_ITEMS
from terranigma_randomizer.utils.logic import create_seeded_rng, create_logical_placement, shuffle_array

def read_chests_from_rom(rom_data):
    """
    Read chest data from ROM
    
    Args:
        rom_data (bytearray): ROM buffer
        
    Returns:
        list: Array of chest objects with current data
    """
    print('Reading chest data from ROM...')
    
    # Create a deep copy of the known chests array to avoid modifying the original
    import copy
    chests = copy.deepcopy(list(CHEST_MAP.values()))
    
    # Read the current item IDs for all chests
    for chest in chests:
        address = chest.get('address')
        if not address or address + 1 >= len(rom_data):
            print(f"Warning: Invalid address {hex(address) if address else 'None'} for chest {chest.get('id')}")
            continue
        
        # Read the item ID (2 bytes)
        item_id_low = rom_data[address + 3]  # CHEST_ITEM_ID_LOW_OFFSET
        item_id_high = rom_data[address + 4]  # CHEST_ITEM_ID_HIGH_OFFSET
        item_id = item_id_low | (item_id_high << 8)
        
        # Update the chest object with current data
        chest['itemID'] = item_id
        chest['itemName'] = get_item_name(item_id)
    
    return chests

def write_chests_to_rom(rom_data, chest_contents):
    """
    Write randomized chest contents to ROM
    
    Args:
        rom_data (bytearray): ROM buffer
        chest_contents (dict): Map of chest IDs to item IDs
        
    Returns:
        bytearray: Modified ROM buffer
    """
    print('Writing randomized chest contents to ROM...')
    
    # Create a copy of the ROM data to modify
    new_rom_data = bytearray(rom_data)
    
    # Apply the randomized contents to each chest
    for chest_id, item_id in chest_contents.items():
        # Find the chest in our known chests
        if chest_id not in CHEST_MAP:
            print(f"Warning: Unknown chest ID {chest_id} - skipping")
            continue
        
        chest = CHEST_MAP[chest_id]
        address = chest.get('address')
        
        if not address or address + 4 >= len(new_rom_data):
            print(f"Warning: Invalid address {hex(address) if address else 'None'} for chest {chest_id} - skipping")
            continue
        
        # Write the item ID (2 bytes)
        new_rom_data[address + 3] = item_id & 0xFF        # Low byte
        new_rom_data[address + 4] = (item_id >> 8) & 0xFF  # High byte
        
        if item_id != chest.get('itemID'):
            print(f"Chest {chest_id}: {chest.get('itemName')} -> {get_item_name(item_id)}")
    
    return new_rom_data

def randomize_chests(rom_data, options):
    """
    Main chest randomizer function
    
    Args:
        rom_data (bytearray): ROM buffer
        options (dict): Randomization options
        
    Returns:
        dict: Modified ROM buffer and spoiler log
    """
    print('\nRandomizing chests...')
    
    # Read current chest data for spoiler log
    current_chests = read_chests_from_rom(rom_data)
    
    # Create RNG with seed
    rng = create_seeded_rng(options.get('seed', random.randint(0, 999999)))
    
    # Create a chest contents mapping
    chest_contents = {}
    
    if options.get('use_logic', True):
        print('Using logical chest placement...')
        # Create a logical placement that ensures the game is beatable
        chest_contents = create_logical_placement(options.get('verbose', False))
        
        if not chest_contents:
            print('Failed to create logical placement, falling back to random placement')
            options['use_logic'] = False
    
    if not options.get('use_logic', True):
        print('Using random chest placement...')
        # Collect all item IDs from the current chests
        all_item_ids = [chest['itemID'] for chest in current_chests]
        
        # Shuffle the items
        shuffle_array(all_item_ids)
        
        # Assign items to chests
        for i, chest in enumerate(current_chests):
            chest_contents[chest['id']] = all_item_ids[i % len(all_item_ids)]
    
    # Write the chest contents to ROM
    modified_rom = write_chests_to_rom(rom_data, chest_contents)
    
    # Create spoiler log
    spoiler_log = []
    for chest in current_chests:
        new_item_id = chest_contents.get(chest['id'], chest['itemID'])
        new_item_name = get_item_name(new_item_id)
        
        spoiler_log.append({
            'chestID': chest['id'],
            'location': f"{chest['mapName'] if 'mapName' in chest else 'Unknown'} ({chest['posX']},{chest['posY']})",
            'originalItem': chest['itemName'],
            'originalItemId': chest['itemID'],
            'newItem': new_item_name,
            'newItemId': new_item_id
        })
    
    return {
        'rom': modified_rom,
        'spoiler_log': spoiler_log
    }