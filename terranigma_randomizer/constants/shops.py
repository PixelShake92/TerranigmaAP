"""
Shop data for Terranigma Randomizer
Contains information about shop locations, contents, and IDs
"""

from terranigma_randomizer.constants.items import ItemTypes

# Known shops in the game
KNOWN_SHOPS = [
    # Shop 0: Crysta Day
    {
        'id': 0,
        'location': 'Crysta Day',
        'mapId': 0x1E,
        'shopPtr16': 0xD04D,
        'fileOffset': 0x19D04D,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0x80, 'name': 'HexRod', 'type': ItemTypes.WEAPON, 'price': 170, 'bcdPrice': 0x0170, 'limit': 1},
            {'itemId': 0xA1, 'name': 'Leather', 'type': ItemTypes.ARMOR, 'price': 190, 'bcdPrice': 0x0190, 'limit': 0}
        ]
    },
    # Shop 1: Crysta Night
    {
        'id': 1,
        'location': 'Crysta Night',
        'mapId': 0x1E,
        'shopPtr16': 0xD062,
        'fileOffset': 0x19D062,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 5, 'bcdPrice': 0x0005, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 8, 'bcdPrice': 0x0008, 'limit': 0},
            {'itemId': 0x80, 'name': 'HexRod', 'type': ItemTypes.WEAPON, 'price': 110, 'bcdPrice': 0x0110, 'limit': 1},
            {'itemId': 0xA1, 'name': 'Leather', 'type': ItemTypes.ARMOR, 'price': 125, 'bcdPrice': 0x0125, 'limit': 1}
        ]
    },
    # Shop 2: Lumina (stage 1)
    {
        'id': 2,
        'location': 'Lumina (stage 1)',
        'mapId': 0x46,
        'shopPtr16': 0xD077,
        'fileOffset': 0x19D077,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0}
        ]
    },
    # Shop 3: Lumina (stage 2/3)
    {
        'id': 3,
        'location': 'Lumina (stage 2/3)',
        'mapId': 0x47,
        'shopPtr16': 0xD084,
        'fileOffset': 0x19D084,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0x82, 'name': 'RaSpear', 'type': ItemTypes.WEAPON, 'price': 240, 'bcdPrice': 0x0240, 'limit': 0},
            {'itemId': 0xA2, 'name': 'LeafSuit', 'type': ItemTypes.ARMOR, 'price': 210, 'bcdPrice': 0x0210, 'limit': 0},
            {'itemId': 0xA3, 'name': 'RaArmr', 'type': ItemTypes.ARMOR, 'price': 380, 'bcdPrice': 0x0380, 'limit': 0}
        ]
    },
    # Shop 5: Sanctuar (birds)
    {
        'id': 5,
        'location': 'Sanctuar (birds)',
        'mapId': 0x4D,
        'shopPtr16': 0xD09D,
        'fileOffset': 0x19D09D,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0xA4, 'name': 'BirdSuit', 'type': ItemTypes.ARMOR, 'price': 550, 'bcdPrice': 0x0550, 'limit': 0}
        ]
    },
    # Shop 6: Sanctuar (pre-birds)
    {
        'id': 6,
        'location': 'Sanctuar (pre-birds)',
        'mapId': 0x4E,
        'shopPtr16': 0xD0AE,
        'fileOffset': 0x19D0AE,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0}
        ]
    },
    # Shop 7: Safarium
    {
        'id': 7,
        'location': 'Safarium',
        'mapId': 0x53,
        'shopPtr16': 0xD0BB,
        'fileOffset': 0x19D0BB,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0x14, 'name': 'Stardew', 'type': ItemTypes.CONSUMABLE, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0}
        ]
    },
    # Shop 8: Indus River
    {
        'id': 8,
        'location': 'Indus River',
        'mapId': 0x38D,
        'shopPtr16': 0xD0CC,
        'fileOffset': 0x19D0CC,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0x14, 'name': 'Stardew', 'type': ItemTypes.CONSUMABLE, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0xA5, 'name': 'FurCoat', 'type': ItemTypes.ARMOR, 'price': 750, 'bcdPrice': 0x0750, 'limit': 0}
        ]
    },
    # Shop 9: Louran Shop
    {
        'id': 9,
        'location': 'Louran Shop',
        'mapId': 0x6E,
        'shopPtr16': 0xD0E1,
        'fileOffset': 0x19D0E1,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0x14, 'name': 'Stardew', 'type': ItemTypes.CONSUMABLE, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x88, 'name': 'BrnzPike', 'type': ItemTypes.WEAPON, 'price': 880, 'bcdPrice': 0x0880, 'limit': 0}
        ]
    },
    # Shop 10: Caravan
    {
        'id': 10,
        'location': 'Caravan',
        'mapId': 0x90,
        'shopPtr16': 0xD0F6,
        'fileOffset': 0x19D0F6,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0x55, 'name': 'Crystal', 'type': ItemTypes.ACCESSORY, 'price': 1000, 'bcdPrice': 0x1000, 'limit': 0}
        ]
    },
    # Shop 11: Caravan
    {
        'id': 11,
        'location': 'Caravan',
        'mapId': 0x90,
        'shopPtr16': 0xD103,
        'fileOffset': 0x19D103,
        'items': [
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0x88, 'name': 'BrnzPike', 'type': ItemTypes.WEAPON, 'price': 880, 'bcdPrice': 0x0880, 'limit': 0},
            {'itemId': 0xAC, 'name': 'VestArmr', 'type': ItemTypes.ARMOR, 'price': 1850, 'bcdPrice': 0x1850, 'limit': 0}
        ]
    },
    # Shop 12: Lhase - Shop
    {
        'id': 12,
        'location': 'Lhase - Shop',
        'mapId': 0x87,
        'shopPtr16': 0xD114,
        'fileOffset': 0x19D114,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0xA8, 'name': 'MonkRobe', 'type': ItemTypes.ARMOR, 'price': 1080, 'bcdPrice': 0x1080, 'limit': 0}
        ]
    },
    # Shop 13: Loire - Shop / Litz - Merchant
    {
        'id': 13,
        'location': 'Loire - Shop',
        'mapId': 0xC7,
        'shopPtr16': 0xD125,
        'fileOffset': 0x19D125,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0x14, 'name': 'Stardew', 'type': ItemTypes.CONSUMABLE, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0}
        ]
    },
    # Shop 14: Loire - Shop Weapons
    {
        'id': 14,
        'location': 'Loire - Shop Weapons',
        'mapId': 0xC7,
        'shopPtr16': 0xD136,
        'fileOffset': 0x19D136,
        'items': [
            {'itemId': 0x88, 'name': 'BrnzPike', 'type': ItemTypes.WEAPON, 'price': 880, 'bcdPrice': 0x0880, 'limit': 0},
            {'itemId': 0x89, 'name': 'LightRod', 'type': ItemTypes.WEAPON, 'price': 980, 'bcdPrice': 0x0980, 'limit': 0},
            {'itemId': 0x8B, 'name': 'SlverPike', 'type': ItemTypes.WEAPON, 'price': 1500, 'bcdPrice': 0x1500, 'limit': 0},
            {'itemId': 0xAA, 'name': 'RingMail', 'type': ItemTypes.ARMOR, 'price': 1280, 'bcdPrice': 0x1280, 'limit': 0}
        ]
    },
    # Shop 15: 1st Ave. - Merchant / Nirlake - House
    {
        'id': 15,
        'location': 'Nirlake - House',
        'mapId': 0xD7,
        'shopPtr16': 0xD147,
        'fileOffset': 0x19D147,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x12, 'name': 'L.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 70, 'bcdPrice': 0x0070, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0x14, 'name': 'Stardew', 'type': ItemTypes.CONSUMABLE, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0}
        ]
    },
    # Shop 16: 1st Ave. - Merchant
    {
        'id': 16,
        'location': '1st Ave. - Merchant',
        'mapId': 0xD7,
        'shopPtr16': 0xD15C,
        'fileOffset': 0x19D15C,
        'items': [
            {'itemId': 0x89, 'name': 'LightRod', 'type': ItemTypes.WEAPON, 'price': 980, 'bcdPrice': 0x0980, 'limit': 0},
            {'itemId': 0x8B, 'name': 'SlverPike', 'type': ItemTypes.WEAPON, 'price': 1500, 'bcdPrice': 0x1500, 'limit': 0},
            {'itemId': 0x86, 'name': 'Icepick', 'type': ItemTypes.WEAPON, 'price': 1770, 'bcdPrice': 0x1770, 'limit': 0},
            {'itemId': 0xAA, 'name': 'RingMail', 'type': ItemTypes.ARMOR, 'price': 1280, 'bcdPrice': 0x1280, 'limit': 0},
            {'itemId': 0xAB, 'name': 'SlverVest', 'type': ItemTypes.ARMOR, 'price': 1550, 'bcdPrice': 0x1550, 'limit': 0},
            {'itemId': 0xAC, 'name': 'VestArmr', 'type': ItemTypes.ARMOR, 'price': 1850, 'bcdPrice': 0x1850, 'limit': 0}
        ]
    },
    # Shop 17: Loire - Merchant
    {
        'id': 17,
        'location': 'Loire - Merchant',
        'mapId': 0xF6,
        'shopPtr16': 0xD175,
        'fileOffset': 0x19D175,
        'items': [
            {'itemId': 0x89, 'name': 'LightRod', 'type': ItemTypes.WEAPON, 'price': 980, 'bcdPrice': 0x0980, 'limit': 0},
            {'itemId': 0x8B, 'name': 'SlverPike', 'type': ItemTypes.WEAPON, 'price': 1500, 'bcdPrice': 0x1500, 'limit': 0},
            {'itemId': 0x86, 'name': 'Icepick', 'type': ItemTypes.WEAPON, 'price': 1770, 'bcdPrice': 0x1770, 'limit': 0}
        ]
    },
    # Shop 18: Freedom - Inn - Merchant
    {
        'id': 18,
        'location': 'Freedom - Inn - Merchant',
        'mapId': 0xF6,
        'shopPtr16': 0xD2A2,
        'fileOffset': 0x19D2A2,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x12, 'name': 'L.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 70, 'bcdPrice': 0x0070, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0x14, 'name': 'Stardew', 'type': ItemTypes.CONSUMABLE, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x15, 'name': 'Serum', 'type': ItemTypes.CONSUMABLE, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x16, 'name': 'H.Water', 'type': ItemTypes.CONSUMABLE, 'price': 90, 'bcdPrice': 0x0090, 'limit': 0}
        ]
    },
    # Shop 19: Loire - Merchant
    {
        'id': 19,
        'location': 'Loire - Merchant',
        'mapId': 0xF6,
        'shopPtr16': 0xD182,
        'fileOffset': 0x19D182,
        'items': [
            {'itemId': 0xAC, 'name': 'VestArmr', 'type': ItemTypes.ARMOR, 'price': 1850, 'bcdPrice': 0x1850, 'limit': 0},
            {'itemId': 0xAE, 'name': 'SlvrArmr', 'type': ItemTypes.ARMOR, 'price': 2500, 'bcdPrice': 0x2500, 'limit': 0},
            {'itemId': 0xB1, 'name': 'DrgnMail', 'type': ItemTypes.ARMOR, 'price': 3880, 'bcdPrice': 0x3880, 'limit': 0}
        ]
    },
    # Shop 20: Loire - Marily's
    {
        'id': 20,
        'location': 'Loire - Marilys',
        'mapId': 0x343,
        'shopPtr16': 0xD18F,
        'fileOffset': 0x19D18F,
        'items': [
            {'itemId': 0xA5, 'name': 'FurCoat', 'type': ItemTypes.ARMOR, 'price': 550, 'bcdPrice': 0x0550, 'limit': 0},
            {'itemId': 0xA9, 'name': 'NiceSuit', 'type': ItemTypes.ARMOR, 'price': 480, 'bcdPrice': 0x0480, 'limit': 0},
            {'itemId': 0xAF, 'name': 'PoshSuit', 'type': ItemTypes.ARMOR, 'price': 1220, 'bcdPrice': 0x1220, 'limit': 0}
        ]
    },
    # Shop 21: Freedom - Inn - Merchant
    {
        'id': 21,
        'location': 'Freedom - Inn - Merchant',
        'mapId': 0x352,
        'shopPtr16': 0xD19C,
        'fileOffset': 0x19D19C,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x12, 'name': 'L.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 70, 'bcdPrice': 0x0070, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0x14, 'name': 'Stardew', 'type': ItemTypes.CONSUMABLE, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0}
        ]
    },
    # Shop 22: Freedom - Inn - Merchant
    {
        'id': 22,
        'location': 'Freedom - Inn - Merchant',
        'mapId': 0x352,
        'shopPtr16': 0xD1B1,
        'fileOffset': 0x19D1B1,
        'items': [
            {'itemId': 0x8B, 'name': 'SlverPike', 'type': ItemTypes.WEAPON, 'price': 1200, 'bcdPrice': 0x1200, 'limit': 0},
            {'itemId': 0x8E, 'name': 'SoulWand', 'type': ItemTypes.WEAPON, 'price': 1650, 'bcdPrice': 0x1650, 'limit': 1},
            {'itemId': 0x86, 'name': 'Icepick', 'type': ItemTypes.WEAPON, 'price': 1770, 'bcdPrice': 0x1770, 'limit': 0},
            {'itemId': 0xAA, 'name': 'RingMail', 'type': ItemTypes.ARMOR, 'price': 1280, 'bcdPrice': 0x1280, 'limit': 0},
            {'itemId': 0xAB, 'name': 'SlverVest', 'type': ItemTypes.ARMOR, 'price': 1550, 'bcdPrice': 0x1550, 'limit': 0},
            {'itemId': 0xAC, 'name': 'VestArmr', 'type': ItemTypes.ARMOR, 'price': 1850, 'bcdPrice': 0x1850, 'limit': 0}
        ]
    },
    # Shop 24: Freedom (Modern) - Weapons
    {
        'id': 24,
        'location': 'Freedom - Weapons',
        'mapId': 0x369,
        'shopPtr16': 0xD1CA,
        'fileOffset': 0x19D1CA,
        'items': [
            {'itemId': 0x8B, 'name': 'SlverPike', 'type': ItemTypes.WEAPON, 'price': 1200, 'bcdPrice': 0x1200, 'limit': 0},
            {'itemId': 0x86, 'name': 'Icepick', 'type': ItemTypes.WEAPON, 'price': 1770, 'bcdPrice': 0x1770, 'limit': 0},
            {'itemId': 0x8D, 'name': 'Trident', 'type': ItemTypes.WEAPON, 'price': 2100, 'bcdPrice': 0x2100, 'limit': 0}
        ]
    },
    # Shop 25: Freedom (Stage 2) - Armor
    {
        'id': 25,
        'location': 'Freedom - Armor (Stage 2)',
        'mapId': 0x36A,
        'shopPtr16': 0xD1D7,
        'fileOffset': 0x19D1D7,
        'items': [
            {'itemId': 0xAC, 'name': 'VestArmr', 'type': ItemTypes.ARMOR, 'price': 1850, 'bcdPrice': 0x1850, 'limit': 0},
            {'itemId': 0xA4, 'name': 'BirdSuit', 'type': ItemTypes.ARMOR, 'price': 1890, 'bcdPrice': 0x1890, 'limit': 0},
            {'itemId': 0xAE, 'name': 'SlvrArmr', 'type': ItemTypes.ARMOR, 'price': 2500, 'bcdPrice': 0x2500, 'limit': 0}
        ]
    },
    # Shop 27: Freedom (Stage 3) - Weapons
    {
        'id': 27,
        'location': 'Freedom - Weapons (Stage 3)',
        'mapId': 0x380,
        'shopPtr16': 0xD1E4,
        'fileOffset': 0x19D1E4,
        'items': [
            {'itemId': 0x8B, 'name': 'SlverPike', 'type': ItemTypes.WEAPON, 'price': 1200, 'bcdPrice': 0x1200, 'limit': 0},
            {'itemId': 0x86, 'name': 'Icepick', 'type': ItemTypes.WEAPON, 'price': 1770, 'bcdPrice': 0x1770, 'limit': 0},
            {'itemId': 0x8F, 'name': 'ThunPike', 'type': ItemTypes.WEAPON, 'price': 2450, 'bcdPrice': 0x2450, 'limit': 0},
            {'itemId': 0x94, 'name': 'LghtPike', 'type': ItemTypes.WEAPON, 'price': 4350, 'bcdPrice': 0x4350, 'limit': 0}
        ]
    },
    # Shop 28: Freedom (Stage 3) - Armor
    {
        'id': 28,
        'location': 'Freedom - Armor',
        'mapId': 0x381,
        'shopPtr16': 0xD1F5,
        'fileOffset': 0x19D1F5,
        'items': [
            {'itemId': 0xAC, 'name': 'VestArmr', 'type': ItemTypes.ARMOR, 'price': 1850, 'bcdPrice': 0x1850, 'limit': 0},
            {'itemId': 0xAE, 'name': 'SlvrArmr', 'type': ItemTypes.ARMOR, 'price': 2500, 'bcdPrice': 0x2500, 'limit': 0},
            {'itemId': 0xA4, 'name': 'BirdSuit', 'type': ItemTypes.ARMOR, 'price': 1890, 'bcdPrice': 0x1890, 'limit': 0},
            {'itemId': 0xB2, 'name': 'SoulArmr', 'type': ItemTypes.ARMOR, 'price': 4450, 'bcdPrice': 0x4450, 'limit': 0}
        ]
    },
    # Shop 30: Litz - Merchant
    {
        'id': 30,
        'location': 'Litz - Merchant',
        'mapId': 0x390,
        'shopPtr16': 0xD206,
        'fileOffset': 0x19D206,
        'items': [
            {'itemId': 0x89, 'name': 'LightRod', 'type': ItemTypes.WEAPON, 'price': 980, 'bcdPrice': 0x0980, 'limit': 0},
            {'itemId': 0x8B, 'name': 'SlverPike', 'type': ItemTypes.WEAPON, 'price': 1200, 'bcdPrice': 0x1200, 'limit': 0},
            {'itemId': 0xAA, 'name': 'RingMail', 'type': ItemTypes.ARMOR, 'price': 1280, 'bcdPrice': 0x1280, 'limit': 0},
            {'itemId': 0xAB, 'name': 'SlverVest', 'type': ItemTypes.ARMOR, 'price': 1550, 'bcdPrice': 0x1550, 'limit': 0}
        ]
    },
    # Shop 32: Litz (Stage Final) - Merchant
    {
        'id': 32,
        'location': 'Litz - Merchant (Stage Final)',
        'mapId': 0x39C,
        'shopPtr16': 0xD217,
        'fileOffset': 0x19D217,
        'items': [
            {'itemId': 0x8B, 'name': 'SlverPike', 'type': ItemTypes.WEAPON, 'price': 1200, 'bcdPrice': 0x1200, 'limit': 0},
            {'itemId': 0x86, 'name': 'Icepick', 'type': ItemTypes.WEAPON, 'price': 1770, 'bcdPrice': 0x1770, 'limit': 0},
            {'itemId': 0xAA, 'name': 'RingMail', 'type': ItemTypes.ARMOR, 'price': 1280, 'bcdPrice': 0x1280, 'limit': 0},
            {'itemId': 0xAB, 'name': 'SlverVest', 'type': ItemTypes.ARMOR, 'price': 1550, 'bcdPrice': 0x1550, 'limit': 0},
            {'itemId': 0xAE, 'name': 'SlvrArmr', 'type': ItemTypes.ARMOR, 'price': 2500, 'bcdPrice': 0x2500, 'limit': 0}
        ]
    },
    # Shop 34: Liotto Store
    {
        'id': 34,
        'location': 'Liotto Store',
        'mapId': 0x3C0,
        'shopPtr16': 0xD22C,
        'fileOffset': 0x19D22C,
        'items': [
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x12, 'name': 'L.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 70, 'bcdPrice': 0x0070, 'limit': 0},
            {'itemId': 0x15, 'name': 'Serum', 'type': ItemTypes.CONSUMABLE, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x14, 'name': 'Stardew', 'type': ItemTypes.CONSUMABLE, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x89, 'name': 'LightRod', 'type': ItemTypes.WEAPON, 'price': 980, 'bcdPrice': 0x0980, 'limit': 0},
            {'itemId': 0x8E, 'name': 'SoulWand', 'type': ItemTypes.WEAPON, 'price': 1650, 'bcdPrice': 0x1650, 'limit': 1},
            {'itemId': 0xAF, 'name': 'PoshSuit', 'type': ItemTypes.ARMOR, 'price': 1220, 'bcdPrice': 0x1220, 'limit': 0}
        ]
    },
    # Shop 35: Yunkou - Merchant
    {
        'id': 35,
        'location': 'Yunkou - Merchant',
        'mapId': 0x3D6,
        'shopPtr16': 0xD249,
        'fileOffset': 0x19D249,
        'items': [
            {'itemId': 0x12, 'name': 'L.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 70, 'bcdPrice': 0x0070, 'limit': 0},
            {'itemId': 0x15, 'name': 'Serum', 'type': ItemTypes.CONSUMABLE, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x14, 'name': 'Stardew', 'type': ItemTypes.CONSUMABLE, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x16, 'name': 'H.Water', 'type': ItemTypes.CONSUMABLE, 'price': 90, 'bcdPrice': 0x0090, 'limit': 0},
            {'itemId': 0x92, 'name': 'DrgnPike', 'type': ItemTypes.WEAPON, 'price': 3150, 'bcdPrice': 0x3150, 'limit': 0},
            {'itemId': 0xB0, 'name': 'KungFuGi', 'type': ItemTypes.ARMOR, 'price': 1220, 'bcdPrice': 0x1220, 'limit': 0}
        ]
    },
    # Shop 36: Suncoast- Left Merchant
    {
        'id': 36,
        'location': 'Suncoast- Left Merchant',
        'mapId': 0x3EE,
        'shopPtr16': 0xD26F,
        'fileOffset': 0x19D26F,
        'items': [
            {'itemId': 0x8F, 'name': 'ThunPike', 'type': ItemTypes.WEAPON, 'price': 2450, 'bcdPrice': 0x2450, 'limit': 0},
            {'itemId': 0xAF, 'name': 'PoshSuit', 'type': ItemTypes.ARMOR, 'price': 1220, 'bcdPrice': 0x1220, 'limit': 0}
        ]
    },
    # Shop 37: Suncoast- Right Merchant
    {
        'id': 37,
        'location': 'Suncoast- Right Merchant',
        'mapId': 0x3EE,
        'shopPtr16': 0xD2A2,
        'fileOffset': 0x19D2A2,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x12, 'name': 'L.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 70, 'bcdPrice': 0x0070, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0x14, 'name': 'Stardew', 'type': ItemTypes.CONSUMABLE, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x15, 'name': 'Serum', 'type': ItemTypes.CONSUMABLE, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x16, 'name': 'H.Water', 'type': ItemTypes.CONSUMABLE, 'price': 90, 'bcdPrice': 0x0090, 'limit': 0}
        ]
    },
    # Shop 38: Suncoast Merchant
    {
        'id': 38,
        'location': 'Suncoast Merchant',
        'mapId': 0x402,
        'shopPtr16': 0xD2A2,
        'fileOffset': 0x19D2A2,
        'items': [
            {'itemId': 0x10, 'name': 'S.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x11, 'name': 'M.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x12, 'name': 'L.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 70, 'bcdPrice': 0x0070, 'limit': 0},
            {'itemId': 0x13, 'name': 'P. Cure', 'type': ItemTypes.CONSUMABLE, 'price': 13, 'bcdPrice': 0x0013, 'limit': 0},
            {'itemId': 0x14, 'name': 'Stardew', 'type': ItemTypes.CONSUMABLE, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x15, 'name': 'Serum', 'type': ItemTypes.CONSUMABLE, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x16, 'name': 'H.Water', 'type': ItemTypes.CONSUMABLE, 'price': 90, 'bcdPrice': 0x0090, 'limit': 0}
        ]
    },
    # Shop 39: Suncoast (Modern) - Merchant
    {
        'id': 39,
        'location': 'Suncoast - Merchant',
        'mapId': 0x402,
        'shopPtr16': 0xD278,
        'fileOffset': 0x19D278,
        'items': [
            {'itemId': 0x90, 'name': 'SeaSpear', 'type': ItemTypes.WEAPON, 'price': 3000, 'bcdPrice': 0x3000, 'limit': 1},
            {'itemId': 0x94, 'name': 'LghtPike', 'type': ItemTypes.WEAPON, 'price': 4350, 'bcdPrice': 0x4350, 'limit': 0},
            {'itemId': 0x9E, 'name': 'AlphaRod', 'type': ItemTypes.WEAPON, 'price': 7500, 'bcdPrice': 0x7500, 'limit': 1},
            {'itemId': 0xB1, 'name': 'DrgnMail', 'type': ItemTypes.ARMOR, 'price': 3880, 'bcdPrice': 0x3880, 'limit': 0},
            {'itemId': 0xB2, 'name': 'SoulArmr', 'type': ItemTypes.ARMOR, 'price': 4450, 'bcdPrice': 0x4450, 'limit': 0}
        ]
    },
    # Shop 40: Mosque - Shop
    {
        'id': 40,
        'location': 'Mosque - Shop',
        'mapId': 0x40E,
        'shopPtr16': 0xD28D,
        'fileOffset': 0x19D28D,
        'items': [
            {'itemId': 0x12, 'name': 'L.Bulb', 'type': ItemTypes.CONSUMABLE, 'price': 130, 'bcdPrice': 0x0130, 'limit': 0},
            {'itemId': 0x14, 'name': 'Stardew', 'type': ItemTypes.CONSUMABLE, 'price': 150, 'bcdPrice': 0x0150, 'limit': 0},
            {'itemId': 0x15, 'name': 'Serum', 'type': ItemTypes.CONSUMABLE, 'price': 140, 'bcdPrice': 0x0140, 'limit': 0},
            {'itemId': 0x16, 'name': 'H.Water', 'type': ItemTypes.CONSUMABLE, 'price': 150, 'bcdPrice': 0x0150, 'limit': 0},
            {'itemId': 0xB5, 'name': 'RedArmr', 'type': ItemTypes.ARMOR, 'price': 6660, 'bcdPrice': 0x6660, 'limit': 0}
        ]
    },
    # Shop 42: Nirlake (Modern) - Hotel - Room 2 (Merchant)
    {
        'id': 42,
        'location': 'Nirlake - Hotel - Room 2',
        'mapId': 0x43D,
        'shopPtr16': 0xD262,
        'fileOffset': 0x19D262,
        'items': [
            {'itemId': 0x94, 'name': 'LghtPike', 'type': ItemTypes.WEAPON, 'price': 4350, 'bcdPrice': 0x4350, 'limit': 0},
            {'itemId': 0xB2, 'name': 'SoulArmr', 'type': ItemTypes.ARMOR, 'price': 4450, 'bcdPrice': 0x4450, 'limit': 0},
            {'itemId': 0xBD, 'name': 'Pro Armr', 'type': ItemTypes.ARMOR, 'price': 7890, 'bcdPrice': 0x7890, 'limit': 1}
        ]
    },
    # Shop 43: Crysta Magic Shop
    {
        'id': 43,
        'location': 'Crysta Magic Shop',
        'mapId': 0x1D,
        'shopPtr16': 0xD2BF,
        'fileOffset': 0x19D2BF,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 5, 'bcdPrice': 0x0005, 'limit': 0},
            {'itemId': 0x03, 'name': 'IceRing', 'type': ItemTypes.RING, 'price': 5, 'bcdPrice': 0x0005, 'limit': 0}
        ]
    },
    # Shop 44: Below Evergreen Ring Shop
    {
        'id': 44,
        'location': 'Below Evergreen Ring Shop',
        'mapId': 0x2D7,
        'shopPtr16': 0xD2C8,
        'fileOffset': 0x19D2C8,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 7, 'bcdPrice': 0x0007, 'limit': 0},
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 9, 'bcdPrice': 0x0009, 'limit': 0}
        ]
    },
    # Shop 45: Loire Ring Shop
    {
        'id': 45,
        'location': 'Loire Ring Shop',
        'mapId': 0xD0,
        'shopPtr16': 0xD304,
        'fileOffset': 0x19D304,
        'items': [
            {'itemId': 0x09, 'name': 'RayRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0A, 'name': 'ElecRing', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 20, 'bcdPrice': 0x0020, 'limit': 0},
            {'itemId': 0x0D, 'name': 'BonePin', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0}
        ]
    },
    # Shop 46: Santuar Pre Birds - Ring Shop
    {
        'id': 46,
        'location': 'Santuar Pre Birds - Ring Shop',
        'mapId': 0x4D,
        'shopPtr16': 0xD2D1,
        'fileOffset': 0x19D2D1,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x02, 'name': 'PyroRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 20, 'bcdPrice': 0x0020, 'limit': 0}
        ]
    },
    # Shop 48: Safarium Ring Shop
    {
        'id': 48,
        'location': 'Safarium - Ring Shop',
        'mapId': 0x53,
        'shopPtr16': 0xD2DE,
        'fileOffset': 0x19D2DE,
        'items': [
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x07, 'name': 'GeoRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x04, 'name': 'SnowRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 35, 'bcdPrice': 0x0035, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0}
        ]
    },
    # Shop 49: Ring Shop
    {
        'id': 49,
        'location': 'Indus River - Ring Shop',
        'mapId': 0x38D,
        'shopPtr16': 0xD2F3,
        'fileOffset': 0x19D2F3,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x02, 'name': 'PyroRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 35, 'bcdPrice': 0x0035, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0}
        ]
    }
]
''' These are kinda complex logic wise to account for so commented out for now. One day definitely. 
    # Shop 50: 1st Ave Magishop 
    {
        'id': 50,
        'location': '1st Ave Magishop',
        'mapId': 0xD8,
        'shopPtr16': 0xD31D,
        'fileOffset': 0x19D31D,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x02, 'name': 'PyroRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x03, 'name': 'IceRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x04, 'name': 'SnowRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x06, 'name': 'BoomRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x09, 'name': 'RayRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0A, 'name': 'ElecRing', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 20, 'bcdPrice': 0x0020, 'limit': 0},
            {'itemId': 0x0D, 'name': 'BonePin', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0}
        ]
    },
    # Shop 51: Loire - Magishop
    {
        'id': 51,
        'location': 'Loire  2/3- Magishop',
        'mapId': 0xF7,
        'shopPtr16': 0xD34A,
        'fileOffset': 0x19D34A,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x02, 'name': 'PyroRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x03, 'name': 'IceRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x04, 'name': 'SnowRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x06, 'name': 'BoomRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x09, 'name': 'RayRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0A, 'name': 'ElecRing', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 20, 'bcdPrice': 0x0020, 'limit': 0},
            {'itemId': 0x0D, 'name': 'BonePin', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0}
        ]
    },
    # Shop 52: Freedom Magishop
    {
        'id': 52,
        'location': 'Freedom Magishop',
        'mapId': 0x353,
        'shopPtr16': 0xD377,
        'fileOffset': 0x19D377,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x03, 'name': 'IceRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 20, 'bcdPrice': 0x0020, 'limit': 0},
            {'itemId': 0x0D, 'name': 'BonePin', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0}
        ]
    },
    # Shop 53: Freedom 2 I think...
    {
        'id': 53,
        'location': 'Freedom 2/3 - Magishop',
        'mapId': 0x353,
        'shopPtr16': 0xD390,
        'fileOffset': 0x19D390,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x03, 'name': 'IceRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 20, 'bcdPrice': 0x0020, 'limit': 0},
            {'itemId': 0x0D, 'name': 'BonePin', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0F, 'name': 'WaterPin', 'type': ItemTypes.RING, 'price': 65, 'bcdPrice': 0x0065, 'limit': 0}
        ]
    },
    # Shop 54: Freedom 2/3 - Magishop
    {
        'id': 54,
        'location': 'Freedom 2/3 - Magishop',
        'mapId': 0x368,
        'shopPtr16': 0xD3AD,
        'fileOffset': 0x19D3AD,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x02, 'name': 'PyroRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x03, 'name': 'IceRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x04, 'name': 'SnowRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x06, 'name': 'BoomRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 20, 'bcdPrice': 0x0020, 'limit': 0},
            {'itemId': 0x0D, 'name': 'BonePin', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0}
        ]
    },
    # Shop 55: Unknown Location
    {
        'id': 55,
        'location': 'Unknown Shop 55',
        'mapId': 0x368,
        'shopPtr16': 0xD3D2,
        'fileOffset': 0x19D3D2,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x02, 'name': 'PyroRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x03, 'name': 'IceRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x04, 'name': 'SnowRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x06, 'name': 'BoomRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 20, 'bcdPrice': 0x0020, 'limit': 0},
            {'itemId': 0x0D, 'name': 'BonePin', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0F, 'name': 'WaterPin', 'type': ItemTypes.RING, 'price': 65, 'bcdPrice': 0x0065, 'limit': 0}
        ]
    },
    # Shop 56: Freedom 3 Magishop
    {
        'id': 56,
        'location': 'Freedom 3 Magishop',
        'mapId': 0x37F,
        'shopPtr16': 0xD434,
        'fileOffset': 0x19D434,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x02, 'name': 'PyroRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x03, 'name': 'IceRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x04, 'name': 'SnowRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x06, 'name': 'BoomRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x07, 'name': 'GeoRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x08, 'name': 'SkyRing', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x09, 'name': 'RayRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0A, 'name': 'ElecRing', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 20, 'bcdPrice': 0x0020, 'limit': 0},
            {'itemId': 0x0D, 'name': 'BonePin', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0F, 'name': 'WaterPin', 'type': ItemTypes.RING, 'price': 65, 'bcdPrice': 0x0065, 'limit': 0},
            {'itemId': 0x0E, 'name': 'HornPin', 'type': ItemTypes.RING, 'price': 50, 'bcdPrice': 0x0050, 'limit': 0}
        ]
    },
    # Shop 57: Unknown Location
    {
        'id': 57,
        'location': 'Yunkou Magishop',
        'mapId': 0x3D5,
        'shopPtr16': 0xD471,
        'fileOffset': 0x19D471,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x02, 'name': 'PyroRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x03, 'name': 'IceRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x04, 'name': 'SnowRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x06, 'name': 'BoomRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x07, 'name': 'GeoRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x08, 'name': 'SkyRing', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x09, 'name': 'RayRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0A, 'name': 'ElecRing', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 20, 'bcdPrice': 0x0020, 'limit': 0},
            {'itemId': 0x0D, 'name': 'BonePin', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0F, 'name': 'WaterPin', 'type': ItemTypes.RING, 'price': 65, 'bcdPrice': 0x0065, 'limit': 0}
        ]
    },
    # Shop 58: Unknown Location
    {
        'id': 58,
        'location': 'Unknown Shop 58',
        'mapId': 0x3D5,
        'shopPtr16': 0xD4AA,
        'fileOffset': 0x19D4AA,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x02, 'name': 'PyroRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x03, 'name': 'IceRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x04, 'name': 'SnowRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x06, 'name': 'BoomRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x07, 'name': 'GeoRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x08, 'name': 'SkyRing', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x09, 'name': 'RayRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0A, 'name': 'ElecRing', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 20, 'bcdPrice': 0x0020, 'limit': 0},
            {'itemId': 0x0D, 'name': 'BonePin', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0F, 'name': 'WaterPin', 'type': ItemTypes.RING, 'price': 65, 'bcdPrice': 0x0065, 'limit': 0},
            {'itemId': 0x0E, 'name': 'HornPin', 'type': ItemTypes.RING, 'price': 50, 'bcdPrice': 0x0050, 'limit': 0}
        ]
    },
    # Shop 59: Unknown Location
    {
        'id': 59,
        'location': 'Unknown Shop 59',
        'mapId': 0x3FC,
        'shopPtr16': 0xD3FB,
        'fileOffset': 0x19D3FB,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x02, 'name': 'PyroRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x03, 'name': 'IceRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x04, 'name': 'SnowRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x06, 'name': 'BoomRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x07, 'name': 'GeoRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x08, 'name': 'SkyRing', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x09, 'name': 'RayRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0A, 'name': 'ElecRing', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 20, 'bcdPrice': 0x0020, 'limit': 0},
            {'itemId': 0x0D, 'name': 'BonePin', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0E, 'name': 'HornPin', 'type': ItemTypes.RING, 'price': 50, 'bcdPrice': 0x0050, 'limit': 0}
        ]
    },
    # Shop 60: Unknown Location
    {
        'id': 60,
        'location': 'Unknown Shop 60',
        'mapId': 0x3FC,
        'shopPtr16': 0xD434,
        'fileOffset': 0x19D434,
        'items': [
            {'itemId': 0x01, 'name': 'FireRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x02, 'name': 'PyroRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x03, 'name': 'IceRing', 'type': ItemTypes.RING, 'price': 10, 'bcdPrice': 0x0010, 'limit': 0},
            {'itemId': 0x04, 'name': 'SnowRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x05, 'name': 'ZapRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x06, 'name': 'BoomRing', 'type': ItemTypes.RING, 'price': 25, 'bcdPrice': 0x0025, 'limit': 0},
            {'itemId': 0x07, 'name': 'GeoRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x08, 'name': 'SkyRing', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x09, 'name': 'RayRing', 'type': ItemTypes.RING, 'price': 15, 'bcdPrice': 0x0015, 'limit': 0},
            {'itemId': 0x0A, 'name': 'ElecRing', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0B, 'name': 'GrassPin', 'type': ItemTypes.RING, 'price': 45, 'bcdPrice': 0x0045, 'limit': 0},
            {'itemId': 0x0C, 'name': 'WindPin', 'type': ItemTypes.RING, 'price': 20, 'bcdPrice': 0x0020, 'limit': 0},
            {'itemId': 0x0D, 'name': 'BonePin', 'type': ItemTypes.RING, 'price': 30, 'bcdPrice': 0x0030, 'limit': 0},
            {'itemId': 0x0F, 'name': 'WaterPin', 'type': ItemTypes.RING, 'price': 65, 'bcdPrice': 0x0065, 'limit': 0},
            {'itemId': 0x0E, 'name': 'HornPin', 'type': ItemTypes.RING, 'price': 50, 'bcdPrice': 0x0050, 'limit': 0}
        ]
    }
'''
# ROM address constants
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

# Create a mapping of shop IDs to their index in the KNOWN_SHOPS array for easier lookup
SHOP_ID_TO_INDEX = {}
for i, shop in enumerate(KNOWN_SHOPS):
    SHOP_ID_TO_INDEX[shop['id']] = i

def decimal_to_bcd(decimal):
    """
    Convert decimal to BCD format
    
    Args:
        decimal (int): Decimal value
        
    Returns:
        int: BCD value
    """
    bcd = 0
    multiplier = 1
    
    # Ensure the value doesn't exceed the maximum representable in BCD
    decimal = min(decimal, 9999)
    
    while decimal > 0:
        digit = decimal % 10
        bcd += digit * multiplier
        multiplier *= 16
        decimal = decimal // 10
    
    return bcd

def bcd_to_decimal(bcd):
    """
    Convert BCD to decimal
    
    Args:
        bcd (int): BCD value
        
    Returns:
        int: Decimal value
    """
    decimal = 0
    multiplier = 1
    
    for i in range(4):
        digit = (bcd >> (i * 4)) & 0xF
        decimal += digit * multiplier
        multiplier *= 10
    
    return decimal