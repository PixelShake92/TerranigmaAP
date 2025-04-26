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
    Apply a highly targeted boss magic patch that only modifies 
    the specific instruction at 0x80BB8B that controls boss magic.
    
    The key finding from the logs is that the instruction at 0x80BB8B
    is indeed the correct one to target, but in a HiROM mapping. 
    
    Args:
        rom_data (bytearray): ROM buffer
        
    Returns:
        bytearray: Modified ROM buffer
    """
    print("Applying precise boss magic patch...")
    
    # Create a copy of the ROM data to modify
    patched_rom = bytearray(rom_data)
    
    # The target BPL instruction in the logs is at 80BB8B in SNES memory
    # Using accurate HiROM mapping (SNES 80xxxx = ROM 00xxxx)
    rom_offset = 0xBB8B  # Direct physical offset in the ROM
    
    # Ensure offset is valid
    if rom_offset >= len(patched_rom):
        print(f"ERROR: Target address 0x{rom_offset:X} is out of range")
        return patched_rom
    
    # Read the current instruction and make sure it's a BPL (0x10)
    current_instruction = patched_rom[rom_offset]
    print(f"Found instruction 0x{current_instruction:02X} at ROM location 0x{rom_offset:X}")
    
    if current_instruction == 0x10:
        # Also check the next byte (branch offset) to make sure it's 0x09
        if patched_rom[rom_offset + 1] == 0x09:
            print(f"Confirmed BPL 0x09 at 0x{rom_offset:X}")
            debug_rom_section(patched_rom, rom_offset, 4)
            
            # Apply the patch: Change BPL (0x10) to BRA (0x80)
            patched_rom[rom_offset] = 0x80
            
            print(f"Modified instruction to BRA at 0x{rom_offset:X}")
            debug_rom_section(patched_rom, rom_offset, 4)
            
            print("Successfully applied boss magic patch")
            return patched_rom
        else:
            print(f"Found BPL at 0x{rom_offset:X}, but with offset 0x{patched_rom[rom_offset+1]:02X} instead of 0x09")
            print("Boss magic patch not applied to avoid incorrect modification")
            return rom_data
    else:
        print(f"Expected BPL (0x10) not found at 0x{rom_offset:X}, found 0x{current_instruction:02X}")
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
        patched_rom = apply_boss_magic_patch(patched_rom)
    
    # Add more patches here as they are developed
    
    return patched_rom