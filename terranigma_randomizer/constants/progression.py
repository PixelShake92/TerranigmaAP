"""
Game progression data for Terranigma Randomizer
Contains information about game areas, progression logic, and shop locations
"""

# Shop locations
SHOP_LOCATIONS = {
    '0': 'Crysta Day',
    '1': 'Crysta Night',
    '2': 'Lumina (stage 1)',
    '3': 'Lumina (stage 2/3)',
    '5': 'Sanctuar (birds)',
    '6': 'Sanctuar (pre-birds)',
    '7': 'Safarium',
    '9': 'Louran Shop',
    '12': 'Lhase - Shop',
    '13': 'Loire - Shop',
    '24': 'Freedom - Weapons',
    '28': 'Freedom - Armor',
    '36': 'Ring Shop',
    '39': 'Suncoast - Merchant'
}

# Map shop locations to shop IDs for logic
SHOP_NAME_TO_ID = {
    'Crysta Day': 'SHOP_CRYSTA_DAY',
    'Crysta Night': 'SHOP_CRYSTA_NIGHT',
    'Lumina (stage 1)': 'SHOP_LUMINA_1',
    'Lumina (stage 2/3)': 'SHOP_LUMINA_2',
    'Sanctuar (birds)': 'SHOP_SANCTUAR_BIRDS',
    'Sanctuar (pre-birds)': 'SHOP_SANCTUAR_PRE',
    'Safarium': 'SHOP_SAFARIUM',
    'Louran Shop': 'SHOP_LOURAN',
    'Lhase - Shop': 'SHOP_LHASE',
    'Loire - Shop': 'SHOP_LOIRE',
    'Loire - Shop Weapons': 'SHOP_LOIRE_WEAPONS',
    'Freedom - Weapons': 'SHOP_FREEDOM_WEAPONS',
    'Freedom - Armor': 'SHOP_FREEDOM_ARMOR',
    'Ring Shop': 'SHOP_RING',
    'Suncoast- Magishop - ': 'SHOP_SUNCOAST_MAGIC',
    'Suncoast - Merchant': 'SHOP_SUNCOAST',
    'Indus River - Ring Shop': 'SHOP_INDUS_RING'
}

# Reverse mapping for displaying shop names
SHOP_ID_TO_NAME = {v: k for k, v in SHOP_NAME_TO_ID.items()}

# Map shop IDs to region requirements - which area must be accessible to reach the shop
SHOP_ID_TO_REGION = {
    'SHOP_CRYSTA_DAY': 'CRYSTA',
    'SHOP_CRYSTA_NIGHT': 'CRYSTA',
    'SHOP_LUMINA_1': 'SURFACE_INITIAL',
    'SHOP_LUMINA_2': 'SURFACE_INITIAL',
    'SHOP_SANCTUAR_BIRDS': 'SURFACE_INITIAL',
    'SHOP_SANCTUAR_PRE': 'SURFACE_INITIAL', 
    'SHOP_SAFARIUM': 'SURFACE_INITIAL',
    'SHOP_INDUS_RING': 'EKLEMATA_REGION',
    'SHOP_LOURAN': 'LOURAN_REGION',
    'SHOP_LHASE': 'NORFEST_REGION',
    'SHOP_LOIRE': 'NORFEST_REGION',
    'SHOP_LOIRE_WEAPONS': 'NORFEST_REGION',
    'SHOP_FREEDOM_WEAPONS': 'NEOTOKYO_SEWER',
    'SHOP_FREEDOM_ARMOR': 'NEOTOKYO_SEWER',
    'SHOP_RING': 'RING_SHOPS',
    'SHOP_SUNCOAST_MAGIC': 'GREAT_LAKES_CAVERN',
    'SHOP_SUNCOAST': 'GREAT_LAKES_CAVERN',

}

# Game progression areas for scaling equipment
GAME_AREAS = [
    # Early game
    ['Crysta Day', 'Crysta Night', 'Lumina (stage 1)'],
    # Mid-early game
    ['Lumina (stage 2/3)', 'Sanctuar (birds)', 'Sanctuar (pre-birds)', 'Safarium'],
    # Mid game
    ['Louran Shop', 'Lhase - Shop', 'Loire - Shop'],
    # Mid-late game
    ['Freedom - Weapons', 'Freedom - Armor'],
    # Late game
    ['Suncoast - Merchant', 'Ring Shop']
]

# Game progression areas - for logic-based chest randomization
PROGRESSION_AREAS = {
    # === EARLY GAME (NO REQUIREMENTS) ===
    
    # Starting areas - accessible from the beginning
    'CRYSTA': {
        'required': [],
        'contains': []
    },
    
    'UNDERWORLD_START': {
        'required': [],
        'contains': [128, 129, 130, 131, 134, 135, 136,] # Tower chests
    },
    
    'TREE_CAVE_ENTRANCE': {
        'required': ['Crystal Thread'],
        'contains': [138, 139, 154, 155, 156, 211, 212, 213, 214, 236, 237] # Initial Tree Cave chests
    },
    
    # Crystal Thread is obtainable early (Tower 4)
    'TOWER4_AREA': {
        'required': ['Crystal Thread'],
        'contains': [137] # Where Crystal Thread is found
    },
    
    # === FIRST PROGRESSION TIER ===
    
    # ElleCape area - requires Crystal Thread, but is needed early
    'ELLE_CAPE_AREA': {
        'required': ['Crystal Thread'],
        'contains': [137] # ElleCape itself isn't in a chest
    },
    
    # Requires Ra Dewdrop (which must be placed in starting areas)
    'TREE_CAVE_INNER': {
        'required': ['Ra Dewdrop'],
        'contains': [140, 141, 164] # Ra Tree inner chambers
    },
    
    # === SECOND PROGRESSION TIER ===
    
    # Giant Leaves area - only accessible after getting Giant Leaves (from starting or tier 1)
    # Also requires ElleCape for some areas
    'SURFACE_INITIAL': {
        'required': ['Giant Leaves', 'ElleCape'],
        'contains': [157, 159, 215, 216, 217, 218, 250] # Initial surface areas
    },
    
    'GRECLIFF_ENTRANCE': {
        'required': ['Giant Leaves', 'ElleCape'],
        'contains': [142] # Entrance to Grecliff
    },
    
    # === THIRD PROGRESSION TIER ===
    
    # Requires RocSpear (which must be placed in tier 1 or earlier)
    'GRECLIFF_MIDDLE': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear'],
        'contains': [158] # Middle section of Grecliff
    },
    
    # === FOURTH PROGRESSION TIER ===
    
    # Requires Sharp Claws (which must be placed in tier 3 or earlier)
    'GRECLIFF_BOSS': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws'],
        'contains': [160, 161, 162, 163] # Boss area of Grecliff
    },
    
    # === FIFTH PROGRESSION TIER (EKLEMATA_REGION) ===
    
    # Post-Grecliff area
    'ZUE': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws'],
        'contains': [165, 166, 167, 168]
    },
    
    # Initial areas after Grecliff
    'EKLEMATA_REGION': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Snowgrass Leaf'],
        'contains': [169, 170, 171, 173, 174, 176, 177, 179]
    },
    
    # Needs Red Scarf (must be placed in tier 4 or earlier)
    'LOURAN_REGION': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Snowgrass Leaf', 'Red Scarf'],
        'contains': [143, 144, 145, 146, 187, 188, 190, 191, 251]
    },
    'NORFEST_REGION': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Snowgrass Leaf', 'Protect Bell'],
        'contains': [180, 201, 202, 203, 204]
    },
    
    # Needs Dog Whistle (must be placed in tier 4 or earlier)
    'STORKOLM_REGION': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Snowgrass Leaf', 'Protect Bell', 'Dog Whistle'],
        'contains': [150, 151]
    },
    
    # === SIXTH PROGRESSION TIER ===
    
    # Requires gems from Sylvain
    'SYLVAIN_CASTLE': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Snowgrass Leaf', 'Red Scarf', 'Protect Bell', 'Ruby', 'Sapphire', 'Black Opal', 'Topaz'],
        'contains': [147, 148, 149, 181, 182, 183, 184, 185]
    },
    
    # Requires Tower Key (which should be obtained from Sylvain)
    'DRAGOON_CASTLE': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Snowgrass Leaf', 'Red Scarf', 'Protect Bell', 'Ruby', 'Sapphire', 'Black Opal', 'Topaz', 'Tower Key'],
        'contains': [193, 194, 195, 196]
    },
    
    # Needs Protect Bell
    'LOIRE_CASTLE': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Snowgrass Leaf', 'Red Scarf', 'Protect Bell', 'Ruby', 'Sapphire', 'Black Opal', 'Topaz', 'Tower Key'],
        'contains': [11]
    },
    
    # === SEVENTH PROGRESSION TIER ===
    
    # Needs Sewer Key
    'NEOTOKYO_SEWER': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Snowgrass Leaf', 'Red Scarf', 'Protect Bell', 'Ruby', 'Sapphire', 'Black Opal', 'Topaz', 'Tower Key', 'Sewer Key'],
        'contains': [153, 198, 199, 200, 209]
    },
    
    # Needs Transceiver
    'NEOTOKYO_ADVANCED': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Snowgrass Leaf', 'Red Scarf', 'Protect Bell', 'Ruby', 'Sapphire', 'Black Opal', 'Topaz', 'Tower Key', 'Sewer Key', 'Transceiver'],
        'contains': []
    },
    
    # === EIGHTH PROGRESSION TIER ===
    
    # Needs Magic Anchor
    'MU_REGION': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Snowgrass Leaf', 'Red Scarf', 'Protect Bell', 'Ruby', 'Sapphire', 'Black Opal', 'Topaz', 'Tower Key', 'Sewer Key', 'Transceiver', 'Magic Anchor'],
        'contains': [234, 235]
    },
    
    # Post Castle Seq
    'MERMAID_TOWER_REGION': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Snowgrass Leaf', 'Red Scarf', 'Protect Bell', 'Ruby', 'Sapphire', 'Black Opal', 'Topaz', 'Tower Key', 'Sewer Key', 'Transceiver', 'Magic Anchor'],
        'contains': [255]
    },
    
    # Great Lakes Cave - requires Engagement Ring first to access Mermaid Tower
    'GREAT_LAKES_CAVERN': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Snowgrass Leaf', 'Red Scarf', 'Protect Bell', 'Ruby', 'Sapphire', 'Black Opal', 'Topaz', 'Tower Key', 'Sewer Key', 'Transceiver', 'Engagement Ring', 'Air Herb', 'Magic Anchor'],
        'contains': [152, 205, 206, 207, 219]
    },
    
    # Needs Speed Shoes
    'HIDDEN_REGIONS': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Snowgrass Leaf', 'Red Scarf', 'Protect Bell', 'Ruby', 'Sapphire', 'Black Opal', 'Topaz', 'Tower Key', 'Sewer Key', 'Transceiver', 'Magic Anchor', 'Air Herb', 'Speed Shoes'],
        'contains': [210, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 231, 232, 233, 238, 239, 240, 241]
    },
    
    # Needs Starstone
    'ASTARICA_REGION': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws','Snowgrass Leaf', 'Red Scarf', 'Protect Bell', 'Ruby', 'Sapphire', 'Black Opal', 'Topaz', 'Tower Key', 'Sewer Key', 'Transceiver', 'Magic Anchor', 'Air Herb', 'Starstones5'],
        'contains': [197, 254]
    },
    
    # Needs Ginseng
    'FYDA_RECOVERY': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Ginseng'],
        'contains': []
    },
    
    # Unknown Ring Shop
    'RING_SHOPS': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws','Snowgrass Leaf', 'Red Scarf', 'Protect Bell', 'Ruby', 'Sapphire', 'Black Opal', 'Topaz', 'Tower Key', 'Sewer Key', 'Transceiver', 'Magic Anchor', 'Air Herb', 'Starstone'],
        'contains': []
    },
    
    # === FINAL TIER ===
    
    # Needs Time Bomb
    'BERUGA_AIRSHIP': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Time Bomb'],
        'contains': []
    },
    
    # Final boss
    'DARK_GAIA': {
        'required': ['Giant Leaves', 'ElleCape', 'RocSpear', 'Sharp Claws', 'Holy Seal'],
        'contains': []
    }
}

# Map of which areas are unlocked by which key items
KEY_ITEM_GATES = {
    'Tower Key': ['DRAGOON_CASTLE'],
    'ElleCape': ['SURFACE_INITIAL', 'GRECLIFF_ENTRANCE'],  # Required for surface world
    'Giant Leaves': ['SURFACE_INITIAL', 'GRECLIFF_ENTRANCE'],
    'Ra Dewdrop': ['TREE_CAVE_INNER'],
    'Sewer Key': ['NEOTOKYO_SEWER'],
    'Starstone': [],
    'Starstones5': ['ASTARICA_REGION'],
    'Magic Anchor': ['MU_REGION'],
    'Speed Shoes': ['HIDDEN_REGIONS'],
    'Air Herb': ['GREAT_LAKES_CAVERN'],
    'Sharp Claws': ['GRECLIFF_BOSS', 'ZUE', 'EKLEMATA_REGION', 'NORFEST_REGION', 'STORKOLM_REGION', 'LOURAN_REGION', 'SYLVAIN_CASTLE', 'DRAGOON_CASTLE', 'LOIRE_CASTLE', 'NEOTOKYO_SEWER', 'NEOTOKYO_ADVANCED', 'MU_REGION', 'GREAT_LAKES_CAVERN', 'HIDDEN_REGIONS', 'ASTARICA_REGION', 'MERMAID_TOWER_REGION', 'FYDA_RECOVERY', 'BERUGA_AIRSHIP', 'DARK_GAIA', 'GREAT_LAKES_CAVERN'],
    'RocSpear': ['GRECLIFF_MIDDLE', 'GRECLIFF_BOSS'],
    'Crystal Thread': ['ELLE_CAPE_AREA', 'TREE_CAVE_ENTRANCE'],
    'Dog Whistle': ['STORKOLM_REGION'],
    'Black Opal': ['SYLVAIN_CASTLE'],
    'Engagement Ring': ['GREAT_LAKES_CAVERN'],
    'Jail Key': ['CASTLE_DUNGEON'],
    'Portrait': [], # Story item, doesn't directly gate an area
    'Protect Bell': ['NORFEST_REGION'],
    'Red Scarf': ['LOURAN_REGION'],
    'Ruby': ['SYLVAIN_CASTLE'],
    'Sapphire': ['SYLVAIN_CASTLE'],
    'Topaz': ['SYLVAIN_CASTLE'],
    'Transceiver': ['NEOTOKYO_ADVANCED'],
    'Starstone1': ['ASTARICA_REGION'],
    'Starstone2': ['ASTARICA_REGION'],
    'Starstone3': ['ASTARICA_REGION'],
    'Starstone4': ['ASTARICA_REGION'], 
    'Starstone5': ['ASTARICA_REGION'],
    'Time Bomb': ['BERUGA_AIRSHIP'],
    'Ginseng': ['FYDA_RECOVERY'],
    'Hero Pike': ['DARK_GAIA']
}

def get_progression_tier(shop_location):
    """
    Determine the game progression tier for a shop location
    
    Args:
        shop_location (str): Shop location name
        
    Returns:
        int: Progression tier (0-4)
    """
    # Check each game area tier to find which one contains this shop
    for tier, area_list in enumerate(GAME_AREAS):
        if shop_location in area_list:
            return tier
    
    # Default to tier 2 (mid-game) if not found
    return 2

def get_accessible_areas(collected_items):
    """
    Get the accessible areas based on currently collected items
    
    Args:
        collected_items (set): Set of item names that have been collected
        
    Returns:
        list: Array of area IDs that are accessible
    """
    # Start with base areas
    accessible_areas = ['CRYSTA', 'UNDERWORLD_START',]
    
    # Keep looping until no new areas are found
    progress = True
    while progress:
        progress = False
        
        # Check each progression area to see if we can access it
        for area_name, area in PROGRESSION_AREAS.items():
            # Skip already accessible areas
            if area_name in accessible_areas:
                continue
            
            # Check if all required items for this area are collected
            can_access = all(item in collected_items for item in area['required'])
            
            if can_access:
                accessible_areas.append(area_name)
                progress = True  # We made progress, so continue checking
    
    return accessible_areas

def get_accessible_chests(collected_items):
    """
    Get all chests that are accessible with the current items
    
    Args:
        collected_items (set): Set of item names that have been collected
        
    Returns:
        list: Array of chest IDs that are accessible
    """
    accessible_areas = get_accessible_areas(collected_items)
    accessible_chests = []
    
    # Get all chests from accessible areas
    for area in accessible_areas:
        if area in PROGRESSION_AREAS and PROGRESSION_AREAS[area]['contains']:
            accessible_chests.extend(PROGRESSION_AREAS[area]['contains'])
    
    return accessible_chests

def get_accessible_shops(collected_items):
    """
    Get all shops that are accessible with the current items
    
    Args:
        collected_items (set): Set of item names that have been collected
        
    Returns:
        list: Array of shop IDs that are accessible
    """
    accessible_areas = get_accessible_areas(collected_items)
    accessible_shops = []
    
    # Check each shop to see if its region is accessible
    for shop_id, region in SHOP_ID_TO_REGION.items():
        if region in accessible_areas:
            accessible_shops.append(shop_id)
    
    return accessible_shops