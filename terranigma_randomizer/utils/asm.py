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