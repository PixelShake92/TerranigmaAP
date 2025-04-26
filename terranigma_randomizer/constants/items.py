"""
Item database and constants for Terranigma Randomizer
"""

# Item Type Classifications
class ItemTypes:
    WEAPON = 'weapon'
    ARMOR = 'armor'
    ACCESSORY = 'accessory'
    CONSUMABLE = 'consumable'
    KEY_ITEM = 'key_item'
    SPECIAL = 'special'
    GEMS = 'gems'
    RING = 'rings'

# Item database with IDs and classifications
ITEM_DATABASE = {
    # Weapons
    '0001': {'name': 'FireRing', 'type': ItemTypes.WEAPON, 'power': 1},
    '0080': {'name': 'HexRod', 'type': ItemTypes.WEAPON, 'power': 1},
    '0081': {'name': 'CrySpear', 'type': ItemTypes.WEAPON, 'power': 2},
    '0082': {'name': 'RaSpear', 'type': ItemTypes.WEAPON, 'power': 3},
    '0083': {'name': 'RocSpear', 'type': ItemTypes.WEAPON, 'power': 3},
    '0084': {'name': 'Sticker', 'type': ItemTypes.WEAPON, 'power': 4},
    '0085': {'name': 'Neo Fang', 'type': ItemTypes.WEAPON, 'power': 4},
    '0086': {'name': 'Icepick', 'type': ItemTypes.WEAPON, 'power': 5},
    '0088': {'name': 'BrnzPike', 'type': ItemTypes.WEAPON, 'power': 5},
    '0089': {'name': 'LightRod', 'type': ItemTypes.WEAPON, 'power': 6},
    '008B': {'name': 'SlverPike', 'type': ItemTypes.WEAPON, 'power': 6},
    '008C': {'name': 'FirePike', 'type': ItemTypes.WEAPON, 'power': 7},
    '008D': {'name': 'Trident', 'type': ItemTypes.WEAPON, 'power': 7},
    '008E': {'name': 'SoulWand', 'type': ItemTypes.WEAPON, 'power': 8},
    '008F': {'name': 'ThunPike', 'type': ItemTypes.WEAPON, 'power': 8},
    '0090': {'name': 'SeaSpear', 'type': ItemTypes.WEAPON, 'power': 9},
    '0091': {'name': 'GeoStaff', 'type': ItemTypes.WEAPON, 'power': 9},
    '0092': {'name': 'DrgnPike', 'type': ItemTypes.WEAPON, 'power': 10},
    '0093': {'name': '3PartRod', 'type': ItemTypes.WEAPON, 'power': 10},
    '0094': {'name': 'LghtPike', 'type': ItemTypes.WEAPON, 'power': 11},
    '0095': {'name': 'Fauchard', 'type': ItemTypes.WEAPON, 'power': 11},
    '0096': {'name': 'X-Spear', 'type': ItemTypes.WEAPON, 'power': 12},
    '009C': {'name': 'HeroPike', 'type': ItemTypes.WEAPON, 'power': 12},
    '009D': {'name': 'EnbuPike', 'type': ItemTypes.WEAPON, 'power': 12},
    '009E': {'name': 'AlphaRod', 'type': ItemTypes.WEAPON, 'power': 12},
    '009F': {'name': 'BlockRod', 'type': ItemTypes.WEAPON, 'power': 12},
    
    # Armor
    '00A0': {'name': 'Clothes', 'type': ItemTypes.ARMOR, 'power': 1},
    '00A1': {'name': 'Leather', 'type': ItemTypes.ARMOR, 'power': 2},
    '00A2': {'name': 'LeafSuit', 'type': ItemTypes.ARMOR, 'power': 3},
    '00A3': {'name': 'RaArmr', 'type': ItemTypes.ARMOR, 'power': 4},
    '00A4': {'name': 'BirdSuit', 'type': ItemTypes.ARMOR, 'power': 5},
    '00A5': {'name': 'FurCoat', 'type': ItemTypes.ARMOR, 'power': 6},
    '00A6': {'name': 'Ice Suit', 'type': ItemTypes.ARMOR, 'power': 7},
    '00A8': {'name': 'MonkRobe', 'type': ItemTypes.ARMOR, 'power': 8},
    '00A9': {'name': 'NiceSuit', 'type': ItemTypes.ARMOR, 'power': 9},
    '00AA': {'name': 'RingMail', 'type': ItemTypes.ARMOR, 'power': 10},
    '00AB': {'name': 'SlverVest', 'type': ItemTypes.ARMOR, 'power': 11},
    '00AC': {'name': 'VestArmr', 'type': ItemTypes.ARMOR, 'power': 11},
    '00AE': {'name': 'SlvrArmr', 'type': ItemTypes.ARMOR, 'power': 12},
    '00AF': {'name': 'PoshSuit', 'type': ItemTypes.ARMOR, 'power': 12},
    '00B0': {'name': 'KungFuGi', 'type': ItemTypes.ARMOR, 'power': 12},
    '00B1': {'name': 'DrgnMail', 'type': ItemTypes.ARMOR, 'power': 12},
    '00B2': {'name': 'SoulArmr', 'type': ItemTypes.ARMOR, 'power': 12},
    '00B3': {'name': 'HolySuit', 'type': ItemTypes.ARMOR, 'power': 12},
    '00B4': {'name': 'KingArmr', 'type': ItemTypes.ARMOR, 'power': 12},
    '00B5': {'name': 'RedArmr', 'type': ItemTypes.ARMOR, 'power': 12},
    '00B6': {'name': 'Rags', 'type': ItemTypes.ARMOR, 'power': 12},
    '00BC': {'name': 'HeroArmr', 'type': ItemTypes.ARMOR, 'power': 12},
    '00BD': {'name': 'Pro Armr', 'type': ItemTypes.ARMOR, 'power': 12},
    '00BE': {'name': 'Sea Mail', 'type': ItemTypes.ARMOR, 'power': 12},
    '00BF': {'name': 'ElleCape', 'type': ItemTypes.ARMOR, 'power': 12},
    
    # Key Items and Accessories
    '0032': {'name': 'Crystal Thread', 'type': ItemTypes.KEY_ITEM},
    '0033': {'name': 'Snowgrass Leaf', 'type': ItemTypes.KEY_ITEM},
    '0034': {'name': 'Red Scarf', 'type': ItemTypes.ACCESSORY},
    '0035': {'name': 'Holy Seal', 'type': ItemTypes.ACCESSORY},
    '0036': {'name': 'Protect Bell', 'type': ItemTypes.KEY_ITEM},
    '0037': {'name': 'Sapphire', 'type': ItemTypes.KEY_ITEM},
    '0038': {'name': 'Black Opal', 'type': ItemTypes.KEY_ITEM},
    '0039': {'name': 'Ruby', 'type': ItemTypes.KEY_ITEM},
    '003A': {'name': 'Topaz', 'type': ItemTypes.KEY_ITEM},
    '003B': {'name': 'Portrait', 'type': ItemTypes.ACCESSORY},
    '003C': {'name': 'Sleep Potion', 'type': ItemTypes.KEY_ITEM},
    '003D': {'name': 'Jail Key', 'type': ItemTypes.KEY_ITEM},
    '003E': {'name': 'Tower Key', 'type': ItemTypes.KEY_ITEM},
    '003F': {'name': 'Ra Dewdrop', 'type': ItemTypes.KEY_ITEM},
    '0040': {'name': 'Royal Letter', 'type': ItemTypes.ACCESSORY},
    '0043': {'name': 'Dog Whistle', 'type': ItemTypes.KEY_ITEM},
    '0047': {'name': 'Transceiver', 'type': ItemTypes.ACCESSORY},
    '0048': {'name': 'Time Bomb', 'type': ItemTypes.KEY_ITEM},
    '0049': {'name': 'Magic Anchor', 'type': ItemTypes.KEY_ITEM},
    '004A': {'name': 'Engagement Ring', 'type': ItemTypes.ACCESSORY},
    '004B': {'name': 'Sewer Key', 'type': ItemTypes.KEY_ITEM},
    '004C': {'name': 'Starstone', 'type': ItemTypes.KEY_ITEM},
    '004E': {'name': 'Fancy Clothes', 'type': ItemTypes.ACCESSORY},
    '004F': {'name': 'Matis Painting', 'type': ItemTypes.ACCESSORY},
    '0050': {'name': 'Mushroom', 'type': ItemTypes.ACCESSORY},
    '0051': {'name': 'Wine', 'type': ItemTypes.ACCESSORY},
    '0052': {'name': 'Tasty Meat', 'type': ItemTypes.ACCESSORY},
    '0053': {'name': 'Camera', 'type': ItemTypes.ACCESSORY},
    '0054': {'name': 'Apartment Key', 'type': ItemTypes.KEY_ITEM},
    '0055': {'name': 'Crystal', 'type': ItemTypes.ACCESSORY},
    '0056': {'name': 'Tinned Sardines', 'type': ItemTypes.ACCESSORY},
    '0057': {'name': 'Airfield Plans', 'type': ItemTypes.ACCESSORY},
    '0058': {'name': 'Ginseng', 'type': ItemTypes.KEY_ITEM},
    '0059': {'name': 'Sleepless Seal', 'type': ItemTypes.ACCESSORY},
    '005A': {'name': 'Pretty Flower', 'type': ItemTypes.ACCESSORY},
    '005B': {'name': 'Fever Medicine', 'type': ItemTypes.ACCESSORY},
    '005C': {'name': 'Tin Sheet', 'type': ItemTypes.ACCESSORY},
    '005D': {'name': 'Nirlake Letter', 'type': ItemTypes.ACCESSORY},
    '005E': {'name': 'Log', 'type': ItemTypes.KEY_ITEM},
    '007B': {'name': 'Speed Shoes', 'type': ItemTypes.KEY_ITEM},
    '007C': {'name': 'Giant Leaves', 'type': ItemTypes.KEY_ITEM},
    '007D': {'name': 'Sharp Claws', 'type': ItemTypes.KEY_ITEM},
    '007E': {'name': 'Air Herb', 'type': ItemTypes.KEY_ITEM},
    
    # Rings
    '0001': {'name': 'FireRing', 'type': ItemTypes.RING, 'power': 1},
    '0002': {'name': 'PyroRing', 'type': ItemTypes.RING, 'power': 2},
    '0003': {'name': 'IceRing', 'type': ItemTypes.RING, 'power': 1},
    '0004': {'name': 'SnowRing', 'type': ItemTypes.RING, 'power': 2},
    '0005': {'name': 'ZapRing', 'type': ItemTypes.RING, 'power': 1},
    '0006': {'name': 'BoomRing', 'type': ItemTypes.RING, 'power': 3},
    '0007': {'name': 'GeoRing', 'type': ItemTypes.RING, 'power': 3},
    '0008': {'name': 'SkyRing', 'type': ItemTypes.RING, 'power': 5},
    '0009': {'name': 'RayRing', 'type': ItemTypes.RING, 'power': 5},
    '000A': {'name': 'ElecRing', 'type': ItemTypes.RING, 'power': 5},
    '000B': {'name': 'GrassPin', 'type': ItemTypes.RING, 'power': 6},
    '000C': {'name': 'WindPin', 'type': ItemTypes.RING, 'power': 6},
    '000D': {'name': 'BonePin', 'type': ItemTypes.RING, 'power': 6},
    '000E': {'name': 'HornPin', 'type': ItemTypes.RING, 'power': 6},
    '000F': {'name': 'WaterPin', 'type': ItemTypes.RING, 'power': 6},
    
    # Consumables
    '0010': {'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'power': 1},
    '0011': {'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'power': 2},
    '0012': {'name': 'L.Bulb', 'type': ItemTypes.CONSUMABLE, 'power': 3},
    '0013': {'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'power': 2},
    '0014': {'name': 'Stardew', 'type': ItemTypes.CONSUMABLE, 'power': 3},
    '0015': {'name': 'Serum', 'type': ItemTypes.CONSUMABLE, 'power': 4},
    '0016': {'name': 'H.Water', 'type': ItemTypes.CONSUMABLE, 'power': 4},
    '0017': {'name': 'STR Potion', 'type': ItemTypes.CONSUMABLE, 'power': 5},
    '0018': {'name': 'DEF Potion', 'type': ItemTypes.CONSUMABLE, 'power': 5},
    '0019': {'name': 'Luck Potion', 'type': ItemTypes.CONSUMABLE, 'power': 5},
    '001A': {'name': 'Life Potion', 'type': ItemTypes.CONSUMABLE, 'power': 6},
    
    # Gems
    '8030': {'name': '30 Gems', 'type': ItemTypes.GEMS, 'value': 30, 'power': 1},
    '8050': {'name': '50 Gems', 'type': ItemTypes.GEMS, 'value': 50, 'power': 1},
    '8100': {'name': '100 Gems', 'type': ItemTypes.GEMS, 'value': 100, 'power': 2},
    '8200': {'name': '200 Gems', 'type': ItemTypes.GEMS, 'value': 200, 'power': 3},
    '8300': {'name': '300 Gems', 'type': ItemTypes.GEMS, 'value': 300, 'power': 4},
    '8500': {'name': '500 Gems', 'type': ItemTypes.GEMS, 'value': 500, 'power': 5},
    '9003': {'name': '1003 Gems', 'type': ItemTypes.GEMS, 'value': 1003, 'power': 8}
}

# List of key items needed for progression
PROGRESSION_KEY_ITEMS = [
    # Chapter 1 key items
    'Sleepless Seal',
    'Crystal Thread',
    'ElleCape',
    'Sharp Claws',
    
    # Chapter 2 key items
    'Giant Leaves',
    'Ra Dewdrop',
    'RocSpear',
    'Snowgrass Leaf',
    
    # Chapter 3 key items
    'Red Scarf',
    'Holy Seal',
    'Protect Bell',
    'Dog Whistle',
    'Ruby',
    'Sapphire',
    'Black Opal',
    'Topaz',
    'Tower Key',
    'Speed Shoes',
    'Engagement Ring',
    'Magic Anchor',
    'Air Herb',
    'Sewer Key',
    'Transceiver',
    
    # Chapter 4 key items
    'Starstone',  # We need 5 of these!
    'Time Bomb',
    
    # Other important items
    'Portrait',
    'Jail Key',
    'Ginseng'
]

# Create a mapping of item names to their IDs for easier lookup
ITEM_NAME_TO_ID = {}
for id_hex, item in ITEM_DATABASE.items():
    if item['name'] not in ITEM_NAME_TO_ID:
        ITEM_NAME_TO_ID[item['name']] = int(id_hex, 16)

# ROM address constants
CHEST_DATA_START = 0x19E14C
CHEST_ENTRY_SIZE = 7
CHEST_POSITION_X_OFFSET = 0
CHEST_POSITION_Y_OFFSET = 1
CHEST_FLAG_TYPE_OFFSET = 2
CHEST_ITEM_ID_LOW_OFFSET = 3
CHEST_ITEM_ID_HIGH_OFFSET = 4
CHEST_ID_LOW_OFFSET = 5
CHEST_ID_HIGH_OFFSET = 6

SHOP_DATA_START = 0x19CE26
SHOP_ENTRY_SIZE = 9
SHOP_MAP_ID_OFFSET = 0
SHOP_POINTER_OFFSET = 4
SHOP_ITEM_LIMIT = 15
SHOP_ITEM_ENTRY_SIZE = 4
SHOP_ITEM_ID_OFFSET = 0
SHOP_PRICE_LOW_OFFSET = 1
SHOP_PRICE_HIGH_OFFSET = 2
SHOP_LIMIT_OFFSET = 3

def get_item_name(item_id):
    """
    Get a human-readable item name from an item ID
    
    Args:
        item_id (int): Item ID from ROM
        
    Returns:
        str: Item name or "Unknown Item" if not found
    """
    id_hex = f"{item_id:04X}"
    
    if id_hex in ITEM_DATABASE:
        return ITEM_DATABASE[id_hex]['name']
    
    # For gem items with high bit set
    gem_id_hex = f"{(item_id | 0x8000):04X}"
    if gem_id_hex in ITEM_DATABASE:
        return ITEM_DATABASE[gem_id_hex]['name']
    
    return f"Unknown Item (0x{id_hex})"

def get_item_info(item_id):
    """
    Get item info from database by ID
    
    Args:
        item_id (int): The item ID
        
    Returns:
        dict: Item information or default values if not found
    """
    hex_id = f"{item_id:04X}"
    return ITEM_DATABASE.get(hex_id, {'name': 'Unknown', 'type': 'Unknown', 'power': 0})