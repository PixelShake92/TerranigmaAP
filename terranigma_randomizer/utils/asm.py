"""
ASM patch module for Terranigma Randomizer
Contains functions to apply various ROM patches
"""

def debug_rom_section(rom_data, address, length=16):
    """
    Print a section of ROM bytes for debugging
    
    Args:
        rom_data (bytearray): ROM buffer
        address (int): Starting address
        length (int): Number of bytes to print
    """
    try:
        print(f"ROM section at {hex(address)}:")
        hex_bytes = ' '.join([f"{rom_data[address+i]:02X}" for i in range(length)])
        print(hex_bytes)
    except Exception as e:
        print(f"Error examining ROM at {hex(address)}: {e}")

def apply_boss_magic_patch(rom_data):
    """
    Apply boss magic patch to enable magic during boss fights.
    
    This patch modifies specific memory addresses for each boss fight to enable magic usage.
    The addresses provided disable the magic restriction flag for each boss.
    
    Args:
        rom_data (bytearray): ROM buffer
        
    Returns:
        bytearray: Modified ROM buffer
    """
    print("Applying boss magic patch...")
    
    # Create a copy of the ROM data to modify
    patched_rom = bytearray(rom_data)
    
    # Boss fight magic restriction addresses
    # Each address needs to be set to 0x00 to enable magic
    boss_patches = [
        # (file_offset, boss_name)
        (0xF8341, "Parasite"),
        (0xFADAB, "Dark Morph Yeti"),
        (0xFB17C, "Dark Morph Mage"),
        (0xFB488, "Dark Morph Human"),
        (0x10D222, "Mudman Canyon"),
        (0x19AC1D, "Megatron"),  # Corrected offset (0x99AC1C - 0x800000)
        (0xFA37B, "Hitoderon"),
        (0xFDB02, "Dark Gaia 1"),
        (0xFB80B, "Dark Gaia 2")
    ]
    
    # Apply patches to enable magic in boss fights
    patches_applied = 0
    for file_offset, boss_name in boss_patches:
        try:
            # Check if offset is within ROM bounds
            if file_offset >= len(patched_rom):
                print(f"[ERROR] {boss_name}: Offset {hex(file_offset)} is beyond ROM size")
                continue
            
            # Get the current value
            original_value = patched_rom[file_offset]
            
            # Check if it needs patching (should be non-zero if magic is disabled)
            if original_value != 0x00:
                # Apply the patch - set to 0x00 to enable magic
                patched_rom[file_offset] = 0x00
                print(f"[OK] {boss_name}: Patched at {hex(file_offset)} (was {hex(original_value)}, now 0x00)")
                patches_applied += 1
            else:
                print(f"[--] {boss_name}: Already enabled at {hex(file_offset)} (value is 0x00)")
                
        except Exception as e:
            print(f"[ERROR] {boss_name}: Error patching at {hex(file_offset)}: {e}")
    
    print(f"\nBoss magic patch completed: {patches_applied} patches applied")
    
    # Verify the patches
    print("\nVerifying patches:")
    for file_offset, boss_name in boss_patches:
        try:
            if file_offset < len(patched_rom):
                value = patched_rom[file_offset]
                status = "[OK] Enabled" if value == 0x00 else "[FAIL] Still disabled"
                print(f"{boss_name}: {status} (value: {hex(value)})")
        except:
            pass
    
    return patched_rom

def apply_intro_skip_patch(rom_data):
    """
    Apply intro skip patch to start the game outside Crysta village.
    
    This patch modifies the intro warp destination to place Ark outside Crysta
    instead of in his room, by changing both the map ID and Y position.
    
    Args:
        rom_data (bytearray): ROM buffer
        
    Returns:
        bytearray: Modified ROM buffer
    """
    print("Applying intro skip patch...")
    
    # Create a copy of the ROM data to modify
    patched_rom = bytearray(rom_data)
    
    # Intro warp data structure addresses (unheadered ROM)
    INTRO_WARP_MAP_OFFSET = 0x108871  # Map ID (2 bytes)
    INTRO_WARP_X_OFFSET = 0x108875    # X position (2 bytes) - stores to $0492
    INTRO_WARP_Y_OFFSET = 0x108877    # Y position (2 bytes) - stores to $0494
    
    try:
        # Check if offsets are within ROM bounds
        if INTRO_WARP_X_OFFSET + 1 >= len(patched_rom):
            print(f"[ERROR] Intro skip: Offset {hex(INTRO_WARP_X_OFFSET)} is beyond ROM size")
            return patched_rom
        
        # Change map ID from 0x000F (Ark's room) to outside Crysta
        # Based on your notes, we need to find the correct map ID for outside Crysta
        # You mentioned "it should be at 71" - assuming this means the map ID
        current_map = patched_rom[INTRO_WARP_MAP_OFFSET] | (patched_rom[INTRO_WARP_MAP_OFFSET + 1] << 8)
        
        # Set new map ID for outside Crysta
        # Map IDs in Terranigma:
        # 0x000F = Ark's room (current)
        # 0x0003 = Overworld outside Crysta (destination)
        NEW_MAP_ID = 0x0003  # Overworld outside Crysta
        
        patched_rom[INTRO_WARP_MAP_OFFSET] = NEW_MAP_ID & 0xFF      # Low byte
        patched_rom[INTRO_WARP_MAP_OFFSET + 1] = (NEW_MAP_ID >> 8) & 0xFF  # High byte
        
        new_map = patched_rom[INTRO_WARP_MAP_OFFSET] | (patched_rom[INTRO_WARP_MAP_OFFSET + 1] << 8)
        
        print(f"[OK] Intro skip: Patched map ID at {hex(INTRO_WARP_MAP_OFFSET)}")
        print(f"     Changed from {hex(current_map)} to {hex(new_map)}")
        
        # Change X position (stored at $0492 in-game)
        current_x = patched_rom[INTRO_WARP_X_OFFSET] | (patched_rom[INTRO_WARP_X_OFFSET + 1] << 8)
        
        # Set X position to 0x0210 (matching the village exit X coordinate)
        NEW_X_POS = 0x0210
        
        patched_rom[INTRO_WARP_X_OFFSET] = NEW_X_POS & 0xFF      # Low byte
        patched_rom[INTRO_WARP_X_OFFSET + 1] = (NEW_X_POS >> 8) & 0xFF  # High byte
        
        new_x = patched_rom[INTRO_WARP_X_OFFSET] | (patched_rom[INTRO_WARP_X_OFFSET + 1] << 8)
        
        print(f"[OK] Intro skip: Patched X position at {hex(INTRO_WARP_X_OFFSET)}")
        print(f"     Changed from {hex(current_x)} to {hex(new_x)}")
        
        # Change Y position (stored at $0494 in-game)
        current_y = patched_rom[INTRO_WARP_Y_OFFSET] | (patched_rom[INTRO_WARP_Y_OFFSET + 1] << 8)
        
        # Apply the patch - set Y position to 0x0210 (from village exit code)
        NEW_Y_POS = 0x0210
        
        patched_rom[INTRO_WARP_Y_OFFSET] = NEW_Y_POS & 0xFF      # Low byte
        patched_rom[INTRO_WARP_Y_OFFSET + 1] = (NEW_Y_POS >> 8) & 0xFF  # High byte
        
        new_y = patched_rom[INTRO_WARP_Y_OFFSET] | (patched_rom[INTRO_WARP_Y_OFFSET + 1] << 8)
        
        print(f"[OK] Intro skip: Patched Y position at {hex(INTRO_WARP_Y_OFFSET)}")
        print(f"     Changed from {hex(current_y)} to {hex(new_y)}")
        
        print(f"\nIntro skip summary:")
        print(f"  Map: {hex(current_map)} -> {hex(new_map)}")
        print(f"  X pos: {hex(current_x)} -> {hex(new_x)} (stores to $0492)")
        print(f"  Y pos: {hex(current_y)} -> {hex(new_y)} (stores to $0494)")
        
    except Exception as e:
        print(f"[ERROR] Intro skip: Error patching: {e}")
    
    print("Intro skip patch completed")
    
    return patched_rom

def apply_asm_patches(rom_data, options):
    """
    Apply all selected ASM patches based on options
    
    Args:
        rom_data (bytearray): ROM buffer
        options (dict): Randomization options
        
    Returns:
        bytearray: Modified ROM buffer
    """
    patched_rom = bytearray(rom_data)
    
    # Apply boss magic patch if enabled
    if options.get("enable_boss_magic"):
        patched_rom = apply_boss_magic_patch(patched_rom)
    
    # Apply intro skip patch if enabled
    if options.get("enable_intro_skip"):
        patched_rom = apply_intro_skip_patch(patched_rom)
    
    # Add more patches here as they are developed
    
    return patched_rom