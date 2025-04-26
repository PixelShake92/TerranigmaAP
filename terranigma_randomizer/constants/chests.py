"""
Chest data for Terranigma Randomizer
Contains information about chest locations, contents, and IDs
"""

from terranigma_randomizer.constants.items import ItemTypes

# List of known chests in the game
KNOWN_CHESTS = [
    # Crysta - Elder's chests (with event flags)
    # {
    #     'address': 0x19e106,  # Based on the chest table data
    #     'id': 1,              # Chest ID
    #     'itemID': 0x8050,     # Current item (50 Gems)
    #     'itemName': "50 Gems",
    #     'posX': 11, 
    #     'posY': 6,
    #     'flagType': 0x80,     # Event flag check
    #     'eventFlag': 0x0025,  # Event flag to check
    #     'mapName': "Crysta - Elder's" 
    # },
    # { 
    #     'address': 0x19e10f,  # Based on the chest table data
    #     'id': 2,              # Chest ID
    #     'itemID': 0x0010,     # Current item (S.Bulb)
    #     'itemName': "S.Bulb",
    #     'posX': 11, 
    #     'posY': 8,
    #     'flagType': 0x80,     # Event flag check
    #     'eventFlag': 0x0025,  # Event flag to check
    #     'mapName': "Crysta - Elder's" 
    # },
    # Louran chest (appears in two maps)
    { 
        'address': 0x19e11a,  # Based on the chest table data
        'id': 6,              # Chest ID
        'itemID': 0x0001,     # Current item (FireRing)
        'itemName': "FireRing",
        'posX': 7, 
        'posY': 26,
        'mapName': "Louran" 
    },
    { 
        'address': 0x19e132,  # Physical address in ROM
        'id': 10,            # Chest ID
        'itemID': 0x10,     # Current item (S.Bulb)
        'itemName': "S.Bulb",
        'posX': 13, 
        'posY': 26,
        'mapName': "Safarium" # Update with correct map name
    },
    # Loire Castle chest
    { 
        'address': 0x19e13a,  # Based on the chest table data
        'id': 11,             # Chest ID
        'itemID': 0x0036,     # Current item (Protect Bell)
        'itemName': "Protect Bell",
        'posX': 55, 
        'posY': 11,
        'mapName': "Loire Castle - Tower - 3rd Floor" 
    },
    { 
        'address': 0x19e44f,  # Based on the chest table data
        'id': 12,             # Chest ID
        'itemID': 0x005C,     # Current item (Tin Sheet)
        'itemName': "Tin Sheet",
        'posX': 22, 
        'posY': 88,
        'flagType': 0x08,     # Flag type value
        'mapName': "Nirlake - House" 
    },
    { 
        'address': 0x19e429,  # Physical address in ROM
        'id': 13,            # Chest ID
        'itemID': 0x12,     # Current item (L.Bulb)
        'itemName': "L.Bulb",
        'posX': 13, 
        'posY': 6,
        'mapName': "Mush (Near Loire)" # Update with correct map name
    },
    { 
        'address': 0x19e430,  # Physical address in ROM
        'id': 14,            # Chest ID
        'itemID': 0x8500,     # Current item (500 Gems)
        'itemName': "500 Gems",
        'posX': 18, 
        'posY': 16,
        'mapName': "Mush (Near Loire)"
    },
    { 
        'address': 0x19e437,  # Based on the chest table data
        'id': 15,             # Chest ID
        'itemID': 0x0050,     # Current item (Mushroom)
        'itemName': "Mushroom",
        'posX': 5, 
        'posY': 26,
        'flagType': 0x08,     # Flag type value (event flag check)
        'mapName': "Mush (Near Loire)" 
    },
    { 
        'address': 0x19e43f,  # Physical address in ROM
        'id': 16,            # Chest ID
        'itemID': 0x19,     # Current item (Luck Potion)
        'itemName': "Luck Potion",
        'posX': 3, 
        'posY': 4,
        'mapName': "Litz" # Update with correct map name
    },
    { 
        'address': 0x19e447,  # Physical address in ROM
        'id': 17,            # Chest ID
        'itemID': 0x1a,     # Current item (Life Potion)
        'itemName': "Life Potion",
        'posX': 11, 
        'posY': 37,
        'mapName': "Nirlake - House" # Update with correct map name
    },
    { 
        'address': 0x19e457,  # Physical address in ROM
        'id': 18,            # Chest ID
        'itemID': 0x12,     # Current item (L.Bulb)
        'itemName': "L.Bulb",
        'posX': 25, 
        'posY': 8,
        'mapName': "Litz - Ship - Storage" # Update with correct map name
    },
    { 
        'address': 0x19e12a,  # Physical address in ROM
        'id': 19,            # Chest ID
        'itemID': 0x14,     # Current item (Stardew)
        'itemName': "Stardew",
        'posX': 57, 
        'posY': 45,
        'mapName': "Lumina" # Update with correct map name
    },
    { 
        'address': 0x19e142,  # Physical address in ROM
        'id': 128,            # Chest ID
        'itemID': 0x10,     # Current item (S.Bulb)
        'itemName': "S.Bulb",
        'posX': 12, 
        'posY': 37,
        'mapName': "Tower 1 - 3rd Floor" # Update with correct map name
    },
    { 
        'address': 0x19e14a,  # Physical address in ROM
        'id': 129,            # Chest ID
        'itemID': 0x8030,     # Current item (30 Gems)
        'itemName': "30 Gems",
        'posX': 35, 
        'posY': 32,
        'mapName': "Tower 2 - 1st Floor"
    },
    { 
        'address': 0x19e152,  # Physical address in ROM
        'id': 130,            # Chest ID
        'itemID': 0x10,     # Current item (S.Bulb)
        'itemName': "S.Bulb",
        'posX': 12, 
        'posY': 32,
        'mapName': "Tower 2 - 2nd Floor" 
    },
    { 
        'address': 0x19e15a,  # Physical address in ROM
        'id': 131,            # Chest ID
        'itemID': 0x10,     # Current item (S.Bulb)
        'itemName': "S.Bulb",
        'posX': 29, 
        'posY': 23,
        'mapName': "Tower 3- 1st Floor" 
    },
    { 
        'address': 0x19e162,  # Based on the chest table data
        'id': 132,            # Chest ID
        'itemID': 0x0059,     # Current item (Sleepless Seal)
        'itemName': "Sleepless Seal",
        'posX': 5, 
        'posY': 31,
        'flagType': 0x08,     # Flag type value
        'mapName': "Tower 3 - 4th Floor" 
    },
    { 
        'address': 0x19e16a,  # Physical address in ROM
        'id': 134,            # Chest ID
        'itemID': 0x8044,     # Current item (44 Gems)
        'itemName': "44 Gems",
        'posX': 5, 
        'posY': 53,
        'mapName': "Tower 4 - -1st Floor"
    },
    { 
        'address': 0x19e172,  # Physical address in ROM
        'id': 135,            # Chest ID
        'itemID': 0x11,     # Current item (M.Bulb)
        'itemName': "M.Bulb",
        'posX': 5, 
        'posY': 24,
        'mapName': "Tower 4 - 2nd Floor"
    },
    { 
        'address': 0x19e179,  # Physical address in ROM
        'id': 136,            # Chest ID
        'itemID': 0x1a,     # Current item (Life Potion)
        'itemName': "Life Potion",
        'posX': 10, 
        'posY': 24,
        'mapName': "Tower 4 - 2nd Floor" 
    },
    { 
        'address': 0x19e181,  # Based on the chest table data
        'id': 137,            # Chest ID
        'itemID': 0x0032,     # Current item (Crystal Thread)
        'itemName': "Crystal Thread",
        'posX': 13, 
        'posY': 8,
        'mapName': "Tower 4 - 3rd Floor" 
    },
    { 
        'address': 0x19e191,  # Physical address in ROM
        'id': 138,            # Chest ID
        'itemID': 0x82,     # Current item (Ra Spear)
        'itemName': "Ra Spear",
        'posX': 18, 
        'posY': 3,
        'mapName': "Tree Cave" 
    },
    { 
        'address': 0x19e1bc,  # Physical address in ROM
        'id': 139,            # Chest ID
        'itemID': 0x11,     # Current item (M.Bulb)
        'itemName': "M.Bulb",
        'posX': 8, 
        'posY': 12,
        'mapName': "Tree Cave"
    },
    { 
        'address': 0x19e1f7,  # Based on the chest table data
        'id': 140,            # Chest ID
        'itemID': 0x007C,     # Current item (Giant Leaves)
        'itemName': "Giant Leaves",
        'posX': 18, 
        'posY': 17,
        'mapName': "Tree cave" 
    },
    { 
        'address': 0x19e1ff,  # Physical address in ROM
        'id': 141,            # Chest ID
        'itemID': 0xa2,     # Current item (LeafSuit)
        'itemName': "LeafSuit",
        'posX': 37, 
        'posY': 4,
        'mapName': "Tree Cave"
    },
    { 
        'address': 0x19e237,  # Based on the reference map data
        'id': 142,            # Chest ID
        'itemID': 0x0083,     # Current item (RocSpear)
        'itemName': "RocSpear",
        'posX': 8, 
        'posY': 5,
        'mapName': "Grecliff - Cave" 
    },
    {
        'address': 0x19e130,
        'id': 143,
        'itemID': 0x0034,
        'itemName': "Red Scarf",
        'posX': 8,
        'posY': 21,
        'mapName': "Louran-Meilins House"
    },
    { 
        'address': 0x19e301,  # Physical address in ROM
        'id': 144,            # Chest ID
        'itemID': 0x11,     # Current item (M.Bulb)
        'itemName': "M.Bulb",
        'posX': 6, 
        'posY': 39,
        'mapName': "Louran - House"
    },
    { 
        'address': 0x19e309,  # Based on the chest table data
        'id': 145,            # Chest ID
        'itemID': 0x0035,     # Current item (Holy Seal)
        'itemName': "Holy Seal",
        'posX': 40, 
        'posY': 21,
        'flagType': 0x08,     # Flag type value
        'mapName': "Louran - House" 
    },
    { 
        'address': 0x19e328,  # Physical address in ROM
        'id': 146,            # Chest ID
        'itemID': 0x89,     # Current item (LightRod)
        'itemName': "LightRod",
        'posX': 27, 
        'posY': 5,
        'mapName': "Louran - House"
    },
    { 
        'address': 0x19e358,  # Based on the chest table data
        'id': 147,            # Chest ID
        'itemID': 0x003E,     # Current item (Tower Key)
        'itemName': "Tower Key",
        'posX': 7, 
        'posY': 6,
        'flagType': 0x08,     # Flag type value
        'mapName': "Sylvain Castle" 
    },
    { 
        'address': 0x19e35f,  # Physical address in ROM
        'id': 148,            # Chest ID
        'itemID': 0x86,     # Current item (Icepick)
        'itemName': "Icepick",
        'posX': 4, 
        'posY': 9,
        'mapName': "Sylvain Castle"
    },
    { 
        'address': 0x19e367,  # Based on the chest table data
        'id': 149,            # Chest ID
        'itemID': 0x0039,     # Current item (Ruby)
        'itemName': "Ruby",
        'posX': 53, 
        'posY': 12,
        'flagType': 0x08,     # Flag type value
        'mapName': "Sylvian Castle" 
    },
    { 
        'address': 0x19e386,  # Based on the chest table data
        'id': 150,            # Chest ID
        'itemID': 0x003B,     # Current item (Portrait)
        'itemName': "Portrait",
        'posX': 11, 
        'posY': 6,
        'flagType': 0x08,     # Flag type value
        'mapName': "Stockholm - House" 
    },
    { 
        'address': 0x19e38d,  # Physical address in ROM
        'id': 151,            # Chest ID
        'itemID': 0x11,     # Current item (M.Bulb)
        'itemName': "M.Bulb",
        'posX': 11, 
        'posY': 8,
        'mapName': "Stockholm - House"
    },
    { 
        'address': 0x19e3b5,  # Based on the chest table data
        'id': 152,            # Chest ID
        'itemID': 0x0049,     # Current item (Magic Anchor)
        'itemName': "Magic Anchor",
        'posX': 2, 
        'posY': 51,
        'flagType': 0x08,     # Flag type value
        'mapName': "Great Lakes Cavern" 
    },

    # Sewer chest
    { 
        'address': 0x19e3d4,  # Based on the chest table data
        'id': 153,            # Chest ID
        'itemID': 0x004B,     # Current item (Sewer Key)
        'itemName': "Sewer Key",
        'posX': 55, 
        'posY': 22,
        'flagType': 0x00,     # Flag type value
        'mapName': "Sewer" 
    },
    { 
        'address': 0x19e198,  # Physical address in ROM
        'id': 154,            # Chest ID
        'itemID': 0x10,     # Current item (S.Bulb)
        'itemName': "S.Bulb",
        'posX': 16, 
        'posY': 5,
        'mapName': "Tree cave" 
    },
    { 
        'address': 0x19e1a6,  # Physical address in ROM
        'id': 155,            # Chest ID
        'itemID': 0x13,     # Current item (P. Cure)
        'itemName': "P. Cure",
        'posX': 40, 
        'posY': 22,
        'mapName': "Tree cave"
    },
    { 
        'address': 0x19e1ad,  # Physical address in ROM
        'id': 156,            # Chest ID
        'itemID': 0x11,     # Current item (M.Bulb)
        'itemName': "M.Bulb",
        'posX': 38, 
        'posY': 6,
        'mapName': "Tree cave" 
    },
    { 
        'address': 0x19e227,  # Physical address in ROM
        'id': 157,            # Chest ID
        'itemID': 0x17,     # Current item (STR Potion)
        'itemName': "STR Potion",
        'posX': 27, 
        'posY': 7,
        'mapName': "Grecliff - Cave"
    },
    { 
        'address': 0x19e22f,  # Physical address in ROM
        'id': 158,            # Chest ID
        'itemID': 0x1a,     # Current item (Life Potion)
        'itemName': "Life Potion",
        'posX': 28, 
        'posY': 27,
        'mapName': "Grecliff - Cave"
    },
    { 
        'address': 0x19e23f,  # Physical address in ROM
        'id': 159,            # Chest ID
        'itemID': 0x19,     # Current item (Luck Potion)
        'itemName': "Luck Potion",
        'posX': 59, 
        'posY': 44,
        'mapName': "Zue" 
    },
    { 
        'address': 0x19e207,  # Physical address in ROM
        'id': 160,            # Chest ID
        'itemID': 0x11,     # Current item (M.Bulb)
        'itemName': "M.Bulb",
        'posX': 27, 
        'posY': 5,
        'mapName': "Grecliff" 
    },
    { 
        'address': 0x19e20f,  # Based on the reference map data
        'id': 161,            # Chest ID
        'itemID': 0x0010,     # Current item (S.Bulb)
        'itemName': "S.Bulb",
        'posX': 19, 
        'posY': 65,
        'mapName': "Grecliff" 
    },
    { 
        'address': 0x19e217,  # Physical address in ROM
        'id': 162,            # Chest ID
        'itemID': 0x8087,     # Current item (87 Gems)
        'itemName': "87 Gems",
        'posX': 29, 
        'posY': 17,
        'mapName': "Grecliff" 
    },
    { 
        'address': 0x19e21f,  # Physical address in ROM
        'id': 163,            # Chest ID
        'itemID': 0x11,     # Current item (M.Bulb)
        'itemName': "M.Bulb",
        'posX': 11, 
        'posY': 7,
        'mapName': "Grecliff" 
    },
    { 
        'address': 0x19e1e8,  # Physical address in ROM
        'id': 164,            # Chest ID
        'itemID': 0x11,     # Current item (M.Bulb)
        'itemName': "M.Bulb",
        'posX': 27, 
        'posY': 30,
        'mapName': "Tree Cave" 
    },
    { 
        'address': 0x19e26d,  # Physical address in ROM
        'id': 165,            # Chest ID
        'itemID': 0x13,     # Current item (P. Cure)
        'itemName': "P. Cure",
        'posX': 4, 
        'posY': 26,
        'mapName': "Zue" 
    },
    { 
        'address': 0x19e275,  # Physical address in ROM
        'id': 166,            # Chest ID
        'itemID': 0x8065,     # Current item (65 Gems)
        'itemName': "65 Gems",
        'posX': 56, 
        'posY': 27,
        'mapName': "Zue" 
    },
    { 
        'address': 0x19e27c,  # Physical address in ROM
        'id': 167,            # Chest ID
        'itemID': 0x1a,     # Current item (Life Potion)
        'itemName': "Life Potion",
        'posX': 57, 
        'posY': 27,
        'mapName': "Zue" 
    },
    { 
        'address': 0x19e283,  # Physical address in ROM
        'id': 168,            # Chest ID
        'itemID': 0x10,     # Current item (S.Bulb)
        'itemName': "S.Bulb",
        'posX': 18, 
        'posY': 37,
        'mapName': "Zue" # Update with correct map name
    },
    { 
        'address': 0x19e28b,  # Physical address in ROM
        'id': 169,            # Chest ID
        'itemID': 0x14,     # Current item (Stardew)
        'itemName': "Stardew",
        'posX': 59, 
        'posY': 39,
        'mapName': "Eklemata" 
    },
    { 
        'address': 0x19e293,  # Physical address in ROM
        'id': 170,            # Chest ID
        'itemID': 0x1a,     # Current item (Life Potion)
        'itemName': "Life Potion",
        'posX': 17, 
        'posY': 29,
        'mapName': "Eklemata" 
    },
    { 
        'address': 0x19e29b,  # Based on the chest table data
        'id': 171,            # Chest ID
        'itemID': 0x8099,     # Current item (99 Gems)
        'itemName': "99 Gems",
        'posX': 6, 
        'posY': 8,
        'flagType': 0x00,     # Flag type value
        'mapName': "Eklemata" 
    },    
    { 
        'address': 0x19e1ef,  # Based on the chest table data
        'id': 172,            # Chest ID
        'itemID': 0x0011,     # Current item (M.Bulb)
        'itemName': "M.Bulb",
        'posX': 2, 
        'posY': 28,
        'mapName': "Tree cave" 
    },
    { 
        'address': 0x19e2a2,  # Based on the chest table data
        'id': 173,            # Chest ID
        'itemID': 0x0014,     # Current item (Stardew)
        'itemName': "Stardew",
        'posX': 21, 
        'posY': 20,
        'flagType': 0x00,     # Flag type value
        'mapName': "Eklemata" 
    },
    {     
        'address': 0x19e2aa,  # Based on the chest table data
        'id': 174,            # Chest ID
        'itemID': 0x00A6,     # Current item (Ice Suit)
        'itemName': "Ice Suit",
        'posX': 8, 
        'posY': 7,
        'flagType': 0x00,     # Flag type value
        'mapName': "Eklemata" 
    },
    { 
        'address': 0x19e2b2,  # Based on the chest table data
        'id': 175,            # Chest ID
        'itemID': 0x0019,     # Current item (Luck Potion)
        'itemName': "Luck Potion",
        'posX': 10, 
        'posY': 19,
        'flagType': 0x00,     # Flag type value
        'mapName': "Eklemata (Unused)" 
    },
    { 
        'address': 0x19e2ba,  # Based on the chest table data
        'id': 176,            # Chest ID
        'itemID': 0x008C,     # Current item (FirePike)
        'itemName': "FirePike",
        'posX': 7, 
        'posY': 41,
        'flagType': 0x00,     # Flag type value
        'mapName': "Eklemata" 
    },
    {     
        'address': 0x19e2c2,  # Based on the chest table data
        'id': 177,            # Chest ID
        'itemID': 0x8100,     # Current item (100 Gems)
        'itemName': "100 Gems",
        'posX': 16, 
        'posY': 6,
        'flagType': 0x00,     # Flag type value
        'mapName': "Eklemata" 
    },
    { 
        'address': 0x19e1e0,  # Based on the chest table data
        'id': 178,            # Chest ID
        'itemID': 0x0013,     # Current item (P. Cure)
        'itemName': "P. Cure",
        'posX': 45, 
        'posY': 7,
        'mapName': "Tree cave" 
    },
    { 
        'address': 0x19e2c9,  # Based on the chest table data
        'id': 179,            # Chest ID
        'itemID': 0x0014,     # Current item (Stardew)
        'itemName': "Stardew",
        'posX': 41, 
        'posY': 8,
        'flagType': 0x00,     # Flag type value
        'mapName': "Eklemata" 
    },
    { 
        'address': 0x19e2d1,  # Based on the chest table data
        'id': 180,            # Chest ID
        'itemID': 0x00AA,     # Current item (RingMail)
        'itemName': "RingMail",
        'posX': 27, 
        'posY': 54,
        'flagType': 0x00,     # Flag type value
        'mapName': "Norfest" 
    },
    { 
        'address': 0x19e340,  # Based on the chest table data
        'id': 181,            # Chest ID
        'itemID': 0x0014,     # Current item (Stardew)
        'itemName': "Stardew",
        'posX': 28, 
        'posY': 17,
        'flagType': 0x00,     # Flag type value
        'mapName': "Sylvian Castle" 
    },
    { 
        'address': 0x19e348,  # Based on the chest table data
        'id': 182,            # Chest ID
        'itemID': 0x0017,     # Current item (STR Potion)
        'itemName': "STR Potion",
        'posX': 15, 
        'posY': 26,
        'flagType': 0x00,     # Flag type value
        'mapName': "Sylvian Castle" 
    },
    { 
        'address': 0x19e36e,  # Based on the chest table data
        'id': 183,            # Chest ID
        'itemID': 0x0012,     # Current item (L.Bulb)
        'itemName': "L.Bulb",
        'posX': 56, 
        'posY': 12,
        'flagType': 0x00,     # Flag type value
        'mapName': "Sylvian Castle" 
    },
    { 
        'address': 0x19e350,  # Based on the chest table data
        'id': 184,            # Chest ID
        'itemID': 0x0018,     # Current item (DEF Potion)
        'itemName': "DEF Potion",
        'posX': 21, 
        'posY': 39,
        'flagType': 0x00,     # Flag type value
        'mapName': "Sylvian Castle" 
    },
    { 
        'address': 0x19e376,  # Based on the chest table data
        'id': 185,            # Chest ID
        'itemID': 0x8651,     # Current item (651 Gems)
        'itemName': "651 Gems",
        'posX': 11, 
        'posY': 31,
        'flagType': 0x00,     # Flag type value
        'mapName': "Sylvian Castle" 
    },
    { 
        'address': 0x19e319,  # Based on the chest table data
        'id': 187,            # Chest ID
        'itemID': 0x00B6,     # Current item (Rags)
        'itemName': "Rags",
        'posX': 29, 
        'posY': 7,
        'flagType': 0x00,     # Flag type value
        'mapName': "Louran - Storage" 
    },
    { 
        'address': 0x19e320,  # Based on the chest table data
        'id': 188,            # Chest ID
        'itemID': 0x0013,     # Current item (P. Cure)
        'itemName': "P. Cure",
        'posX': 29, 
        'posY': 9,
        'flagType': 0x00,     # Flag type value
        'mapName': "Louran - Storage" 
    },
    { 
        'address': 0x19e330,  # Based on the chest table data
        'id': 190,            # Chest ID
        'itemID': 0x0012,     # Current item (L.Bulb)
        'itemName': "L.Bulb",
        'posX': 21, 
        'posY': 4,
        'flagType': 0x00,     # Flag type value
        'mapName': "Louran - House" 
    },

    # Louran - north side - room chest
    { 
        'address': 0x19e338,  # Based on the chest table data
        'id': 191,            # Chest ID
        'itemID': 0x8178,     # Current item (178 Gems)
        'itemName': "178 Gems",
        'posX': 4, 
        'posY': 21,
        'flagType': 0x00,     # Flag type value
        'mapName': "Louran - north side - room" 
    },
    { 
        'address': 0x19e39d,  # Based on the chest table data
        'id': 192,            # Chest ID
        'itemID': 0x00B2,     # Current item (SoulArmr)
        'itemName': "SoulArmr",
        'posX': 32, 
        'posY': 9,
        'flagType': 0x00,     # Flag type value
        'mapName': "Lab - 1F" 
    },

    # Castle chests
    { 
        'address': 0x19e45f,  # Based on the chest table data
        'id': 193,            # Chest ID
        'itemID': 0x8200,     # Current item (200 Gems)
        'itemName': "200 Gems",
        'posX': 44, 
        'posY': 6,
        'flagType': 0x00,     # Flag type value
        'mapName': "Dragoon Castle - 1st Floor - Room 1" 
    },
    { 
        'address': 0x19e467,  # Based on the chest table data
        'id': 194,            # Chest ID
        'itemID': 0x8300,     # Current item (300 Gems)
        'itemName': "300 Gems",
        'posX': 34, 
        'posY': 41,
        'flagType': 0x00,     # Flag type value
        'mapName': "Dragoon Castle - -1st Floor - Room 2" 
    },
    { 
        'address': 0x19e46e,  # Based on the chest table data
        'id': 195,            # Chest ID
        'itemID': 0x0012,     # Current item (L.Bulb)
        'itemName': "L.Bulb",
        'posX': 32, 
        'posY': 48,
        'flagType': 0x00,     # Flag type value
        'mapName': "Dragoon Castle - -1st Floor - Room 2" 
    },
    {     
        'address': 0x19e476,  # Based on the chest table data
        'id': 196,            # Chest ID
        'itemID': 0x0093,     # Current item (PartRod)
        'itemName': "PartRod",
        'posX': 47, 
        'posY': 43,
        'flagType': 0x00,     # Flag type value
        'mapName': "Dragoon Castle - -1st Floor - Room 3 - A" 
    },

    # Astarica - backroom chest
    { 
        'address': 0x19e403,  # Based on the chest table data
        'id': 197,            # Chest ID
        'itemID': 0x00B3,     # Current item (HolySuit)
        'itemName': "HolySuit",
        'posX': 15, 
        'posY': 41,
        'flagType': 0x00,     # Flag type value
        'mapName': "Astarica - backroom" 
    },
    { 
        'address': 0x19e3dc,  # Based on the chest table data
        'id': 198,            # Chest ID
        'itemID': 0x0016,     # Current item (H.Water)
        'itemName': "H.Water",
        'posX': 20, 
        'posY': 4,
        'flagType': 0x00,     # Flag type value
        'mapName': "Sewer" 
    },
    { 
        'address': 0x19e3e4,  # Based on the chest table data
        'id': 199,            # Chest ID
        'itemID': 0x0095,     # Current item (Fauchard)
        'itemName': "Fauchard",
        'posX': 39, 
        'posY': 5,
        'flagType': 0x00,     # Flag type value
        'mapName': "Sewer" 
    },
    { 
        'address': 0x19e3eb,  # Based on the chest table data
        'id': 200,            # Chest ID
        'itemID': 0x0019,     # Current item (Luck Potion)
        'itemName': "Luck Potion",
        'posX': 21, 
        'posY': 37,
        'flagType': 0x00,     # Flag type value
        'mapName': "Sewer" 
    },

    # Norfest chests
    { 
        'address': 0x19e2d9,  # Based on the chest table data
        'id': 201,            # Chest ID
        'itemID': 0x001A,     # Current item (Life Potion)
        'itemName': "Life Potion",
        'posX': 7, 
        'posY': 53,
        'flagType': 0x00,     # Flag type value
        'mapName': "Norfest" 
    },
    { 
        'address': 0x19e2e1,  # Based on the chest table data
        'id': 202,            # Chest ID
        'itemID': 0x8389,     # Current item (389 Gems)
        'itemName': "389 Gems",
        'posX': 20, 
        'posY': 12,
        'flagType': 0x00,     # Flag type value
        'mapName': "Norfest" 
    },
    {     
        'address': 0x19e2e9,  # Based on the chest table data
        'id': 203,            # Chest ID
        'itemID': 0x0043,     # Current item (Dog Whistle)
        'itemName': "Dog Whistle",
        'posX': 16, 
        'posY': 25,
        'flagType': 0x08,     # Flag type value
        'mapName': "Norfest" 
    },
    {     
        'address': 0x19e2f1,  # Based on the chest table data
        'id': 204,            # Chest ID
        'itemID': 0x0011,     # Current item (M.Bulb)
        'itemName': "M.Bulb",
        'posX': 22, 
        'posY': 6,
        'flagType': 0x00,     # Flag type value
        'mapName': "Norfest" 
    },
    { 
        'address': 0x19e3bc,  # Based on the chest table data
        'id': 205,            # Chest ID
        'itemID': 0x8753,     # Current item (753 Gems)
        'itemName': "753 Gems",
        'posX': 25, 
        'posY': 6,
        'flagType': 0x00,     # Flag type value
        'mapName': "Great Lakes Cavern" 
    },
    { 
        'address': 0x19e3ad,  # Based on the chest table data
        'id': 206,            # Chest ID
        'itemID': 0x007E,     # Current item (Air Herb)
        'itemName': "Air Herb",
        'posX': 7, 
        'posY': 37,
        'flagType': 0x08,     # Flag type value
        'mapName': "Great Lakes Cavern" 
    },
    { 
        'address': 0x19e3c4,  # Based on the chest table data
        'id': 207,            # Chest ID
        'itemID': 0x0091,     # Current item (GeoStaff)
        'itemName': "GeoStaff",
        'posX': 12, 
        'posY': 5,
        'flagType': 0x00,     # Flag type value
        'mapName': "Great Lakes Cavern" 
    },

    # Labtower chest
    { 
        'address': 0x19e3fb,  # Based on the chest table data
        'id': 208,            # Chest ID
        'itemID': 0x001A,     # Current item (Life Potion)
        'itemName': "Life Potion",
        'posX': 4, 
        'posY': 5,
        'flagType': 0x00,     # Flag type value
        'mapName': "Labtower" 
    },

    # Sewer chest
    { 
        'address': 0x19e3f3,  # Based on the chest table data
        'id': 209,            # Chest ID
        'itemID': 0x00B4,     # Current item (KingArmr)
        'itemName': "KingArmr",
        'posX': 5, 
        'posY': 25,
        'flagType': 0x00,     # Flag type value
        'mapName': "Sewer" 
    },

    # Hidden area chest
    { 
        'address': 0x19e40b,  # Based on the chest table data
        'id': 210,            # Chest ID
        'itemID': 0x007B,     # Current item (Speed Shoes)
        'itemName': "Speed Shoes",
        'posX': 11, 
        'posY': 4,
        'flagType': 0x08,     # Flag type value
        'mapName': "Hidden area" 
    },
    { 
        'address': 0x19e1c3,  # Based on the chest table data
        'id': 211,            # Chest ID
        'itemID': 0x0013,     # Current item (P. Cure)
        'itemName': "P. Cure",
        'posX': 13, 
        'posY': 6,
        'mapName': "Tree cave" 
    },
    { 
        'address': 0x19e1ca,  # Based on the chest table data
        'id': 212,            # Chest ID
        'itemID': 0x001A,     # Current item (Life Potion)
        'itemName': "Life Potion",
        'posX': 3, 
        'posY': 9,
        'mapName': "Tree cave" 
    },
    { 
        'address': 0x19e19f,  # Physical address in ROM
        'id': 213,            # Chest ID
        'itemID': 0x13,     # Current item (P. Cure)
        'itemName': "P. Cure",
        'posX': 31, 
        'posY': 7,
        'mapName': "Tree cave"
    },
    { 
        'address': 0x19e1b4,  # Physical address in ROM
        'id': 214,            # Chest ID
        'itemID': 0x10,     # Current item (S.Bulb)
        'itemName': "S.Bulb",
        'posX': 19, 
        'posY': 20,
        'mapName': "Tree cave" 
    },
    { 
        'address': 0x19e256,  # Based on the chest table data
        'id': 215,            # Chest ID
        'itemID': 0x0018,     # Current item (DEF Potion)
        'itemName': "DEF Potion",
        'posX': 15, 
        'posY': 32,
        'flagType': 0x00,     # Flag type value
        'mapName': "Zue" 
    },
    { 
        'address': 0x19e247,  # Based on the chest table data
        'id': 216,            # Chest ID
        'itemID': 0x0013,     # Current item (P. Cure)
        'itemName': "P. Cure",
        'posX': 60, 
        'posY': 11,
        'flagType': 0x00,     # Flag type value
        'mapName': "Zue" 
    },
    { 
        'address': 0x19e24e,  # Based on the chest table data
        'id': 217,            # Chest ID
        'itemID': 0x0011,     # Current item (M.Bulb)
        'itemName': "M.Bulb",
        'posX': 61, 
        'posY': 11,
        'flagType': 0x00,     # Flag type value
        'mapName': "Zue" 
    },
    { 
        'address': 0x19e25e,  # Based on the chest table data
        'id': 218,            # Chest ID
        'itemID': 0x0084,     # Current item (Sticker)
        'itemName': "Sticker",
        'posX': 59, 
        'posY': 4,
        'flagType': 0x00,     # Flag type value
        'mapName': "Zue" 
    },
    { 
        'address': 0x19e3cc,  # Based on the chest table data
        'id': 219,            # Chest ID
        'itemID': 0x00B1,     # Current item (DrgnMail)
        'itemName': "DrgnMail",
        'posX': 57, 
        'posY': 6,
        'flagType': 0x00,     # Flag type value
        'mapName': "Great Lakes Cavern" 
    },

    # Hidden area chests
    {     
        'address': 0x19e47e,  # Based on the chest table data
        'id': 220,            # Chest ID
        'itemID': 0x001A,     # Current item (Life Potion)
        'itemName': "Life Potion",
        'posX': 23, 
        'posY': 18,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area" 
    },
    {     
        'address': 0x19e485,  # Based on the chest table data
        'id': 221,            # Chest ID
        'itemID': 0x8378,     # Current item (378 Gems)
        'itemName': "378 Gems",
        'posX': 9, 
        'posY': 13,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area" 
    },
    { 
        'address': 0x19e48d,  # Based on the chest table data
        'id': 222,            # Chest ID
        'itemID': 0x0011,     # Current item (M.Bulb)
        'itemName': "M.Bulb",
        'posX': 21, 
        'posY': 18,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area" 
    },
    { 
        'address': 0x19e494,  # Based on the chest table data
        'id': 223,            # Chest ID
        'itemID': 0x8378,     # Current item (378 Gems)
        'itemName': "378 Gems",
        'posX': 23, 
        'posY': 20,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area" 
    },
    { 
        'address': 0x19e49c,  # Based on the chest table data
        'id': 224,            # Chest ID
        'itemID': 0x0017,     # Current item (STR Potion)
        'itemName': "STR Potion",
        'posX': 3, 
        'posY': 5,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area" 
    },
    { 
        'address': 0x19e4a4,  # Based on the chest table data
        'id': 225,            # Chest ID
        'itemID': 0x001A,     # Current item (Life Potion)
        'itemName': "Life Potion",
        'posX': 6, 
        'posY': 7,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area near Odemrock" 
    },
    { 
        'address': 0x19e4ab,  # Based on the chest table data
        'id': 226,            # Chest ID
        'itemID': 0x8228,     # Current item (228 Gems)
        'itemName': "228 Gems",
        'posX': 1, 
        'posY': 9,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area near Odemrock" 
    },
    { 
        'address': 0x19e412,  # Based on the chest table data
        'id': 227,            # Chest ID
        'itemID': 0x8378,     # Current item (378 Gems)
        'itemName': "378 Gems",
        'posX': 6, 
        'posY': 5,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area" 
    },
    { 
        'address': 0x19e4b3,  # Based on the chest table data
        'id': 228,            # Chest ID
        'itemID': 0x0019,     # Current item (Luck Potion)
        'itemName': "Luck Potion",
        'posX': 3, 
        'posY': 4,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area" 
    },
    { 
        'address': 0x19e4ba,  # Based on the chest table data
        'id': 229,            # Chest ID
        'itemID': 0x9403,     # Current item (1403 Gems)
        'itemName': "1403 Gems",
        'posX': 26, 
        'posY': 13,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area" 
    },
    { 
        'address': 0x19e4c2,  # Based on the chest table data
        'id': 231,            # Chest ID
        'itemID': 0x009F,     # Current item (BlockRod)
        'itemName': "BlockRod",
        'posX': 27, 
        'posY': 25,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area - near tower" 
    },

    # Hidden area - Sahara chests
    {     
        'address': 0x19e4ca,  # Based on the chest table data
        'id': 232,            # Chest ID
        'itemID': 0x8703,     # Current item (703 Gems)
        'itemName': "703 Gems",
        'posX': 6, 
        'posY': 10,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area - Sahara" 
    },
    { 
        'address': 0x19e4d1,  # Based on the chest table data
        'id': 233,            # Chest ID
        'itemID': 0x9003,     # Current item (1003 Gems)
        'itemName': "1003 Gems",
        'posX': 7, 
        'posY': 26,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area - Sahara" 
    },

    # Mu chests
    { 
        'address': 0x19e4d9,  # Based on the chest table data
        'id': 234,            # Chest ID
        'itemID': 0x0018,     # Current item (DEF Potion)
        'itemName': "DEF Potion",
        'posX': 5, 
        'posY': 4,
        'flagType': 0x00,     # Flag type value
        'mapName': "Mu" 
    },
    { 
        'address': 0x19e4e0,  # Based on the chest table data
        'id': 235,            # Chest ID
        'itemID': 0x009D,     # Current item (EnbuPike)
        'itemName': "EnbuPike",
        'posX': 7, 
        'posY': 22,
        'flagType': 0x00,     # Flag type value
        'mapName': "Mu" 
    },
    { 
        'address': 0x19e1d2,  # Based on the chest table data
        'id': 236,            # Chest ID
        'itemID': 0x0010,     # Current item (S.Bulb)
        'itemName': "S.Bulb",
        'posX': 4, 
        'posY': 4,
        'mapName': "Tree cave" 
    },
    { 
        'address': 0x19e1d9,  # Based on the chest table data
        'id': 237,            # Chest ID
        'itemID': 0x8042,     # Current item (42 Gems)
        'itemName': "42 Gems",
        'posX': 20, 
        'posY': 5,
        'mapName': "Tree cave" 
    },
    { 
        'address': 0x19e4e8,  # Based on the chest table data
        'id': 238,            # Chest ID
        'itemID': 0x8961,     # Current item (961 Gems)
        'itemName': "961 Gems",
        'posX': 3, 
        'posY': 10,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area" 
    },
    { 
        'address': 0x19e4f0,  # Based on the chest table data
        'id': 239,            # Chest ID
        'itemID': 0x001A,     # Current item (Life Potion)
        'itemName': "Life Potion",
        'posX': 8, 
        'posY': 27,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area - Part 2" 
    },
    { 
        'address': 0x19e4f7,  # Based on the chest table data
        'id': 240,            # Chest ID
        'itemID': 0x00BE,     # Current item (Sea Mail)
        'itemName': "Sea Mail",
        'posX': 4, 
        'posY': 27,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area - Part 2" 
    },

    # Hidden area near Odemrock (Zoe like) chest
    { 
        'address': 0x19e4ff,  # Based on the chest table data
        'id': 241,            # Chest ID
        'itemID': 0x8892,     # Current item (892 Gems)
        'itemName': "892 Gems",
        'posX': 22, 
        'posY': 6,
        'flagType': 0x00,     # Flag type value
        'mapName': "Hidden area near Odemrock (Zoe like)" 
    },

    # Lab - 1F chest
    { 
        'address': 0x19e3a5,  # Based on the chest table data
        'id': 252,            # Chest ID
        'itemID': 0x0018,     # Current item (DEF Potion)
        'itemName': "DEF Potion",
        'posX': 11, 
        'posY': 60,
        'flagType': 0x00,     # Flag type value
        'mapName': "Lab - 1F" 
    },

    # Mermaid Tower - 1st sub floor chest
    { 
        'address': 0x19e395,  # Based on the chest table data
        'id': 255,            # Chest ID
        'itemID': 0x0090,     # Current item (SeaSpear)
        'itemName': "SeaSpear",
        'posX': 38, 
        'posY': 19,
        'flagType': 0x00,     # Flag type value
        'mapName': "Mermaid Tower - 1st sub floor" 
    },
    { 
        'address': 0x19e265,  # Based on the chest table data
        'id': 250,            # Chest ID
        'itemID': 0x0011,     # Current item (M.Bulb)
        'itemName': "M.Bulb",
        'posX': 60, 
        'posY': 4,
        'flagType': 0x00,     # Flag type value
        'mapName': "Zue" 
    },
    { 
        'address': 0x19e311,  # Based on the chest table data
        'id': 251,            # Chest ID
        'itemID': 0x0017,     # Current item (STR Potion)
        'itemName': "STR Potion",
        'posX': 20, 
        'posY': 41,
        'flagType': 0x00,     # Flag type value
        'mapName': "Louran north side (Zombies)" 
    },
    # Astarika chest
    { 
        'address': 0x19e189,  # Based on the chest table data
        'id': 254,            # Chest ID
        'itemID': 0x004C,     # Current item (Starstone)
        'itemName': "Starstone",
        'posX': 5, 
        'posY': 6,
        'mapName': "Astarika" 
    },
]

# Create a mapping of chests by ID for easier access
CHEST_MAP = {}
for chest in KNOWN_CHESTS:
    CHEST_MAP[chest['id']] = chest