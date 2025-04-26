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
    Apply a boss magic patch by nullifying the flag instead of changing the branch.
    
    Rather than modifying the branch instruction itself, this patch
    prevents the boss magic flag from being set in the first place.
    
    Args:
        rom_data (bytearray): ROM buffer
        
    Returns:
        bytearray: Modified ROM buffer
    """
    print("Applying boss magic prevention patch...")
    
    # Create a copy of the ROM data to modify
    patched_rom = bytearray(rom_data)
    
    # - STA $3F (85 3F)  - Store accumulator to $3F
    # - ORA $3F (05 3F)  - OR with $3F and store result
    # - AND $3F (25 3F)  - AND with $3F and store result
    
    potential_patches = []
    for i in range(len(patched_rom) - 2):
        # Look for STA $3F (85 3F)
        if patched_rom[i] == 0x85 and patched_rom[i + 1] == 0x3F:
            potential_patches.append(i)
        # Look for ORA $3F (05 3F)
        elif patched_rom[i] == 0x05 and patched_rom[i + 1] == 0x3F:
            potential_patches.append(i)
        # Look for AND $3F (25 3F)
        elif patched_rom[i] == 0x25 and patched_rom[i + 1] == 0x3F:
            potential_patches.append(i)
    
    if potential_patches:
        print(f"Found {len(potential_patches)} potential instructions that modify $3F")
        print("Instead of patching the BPL instruction which affects multiple game systems,")
        print("consider patching where the boss magic flag is set.")
        
        print("\nSafe approach: Insert a NOP at the location that sets the boss magic flag")
        print("This requires further ROM analysis to identify the exact instruction.")
        
        # This would require further analysis of the ROM to identify which instruction
        # specifically sets the boss magic flag, rather than other uses of $3F
        
        # For now, return without modifying the ROM to avoid breaking the game
        return rom_data
    else:
        print("Could not find instructions that modify address $3F")
        print("Boss magic patch not applied")
        return rom_data


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
        print("\nWARNING: The boss magic patch is currently disabled because modifying")
        print("the branch instruction at 0xBB8B affects multiple game systems, including")
        print("progression at the Elder's house and menu graphics.")
        print("Future versions will require finding where the boss magic flag is set.")
        
        # Don't apply the patch to preserve game functionality
        # patched_rom = apply_boss_magic_patch(patched_rom)
    
    # Add more patches here as they are developed
    
    return patched_rom
