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

def apply_autoheal_patch(rom_data):
    """
    Apply autoheal patch to maintain autoheal after Chapter 2.
    
    The game normally disables autoheal by setting [07EF] = 0 in the script of map 0129
    (Chapter 2 intro screen). This patch prevents that from happening.
    
    There are a few approaches:
    1. NOP out the instruction that sets [07EF] = 0
    2. Always set [07EF] = 1 after the chapter transition
    3. Modify the map script to skip the autoheal disable
    
    We'll use approach 1 - find and NOP the instruction that clears autoheal.
    
    Args:
        rom_data (bytearray): ROM buffer
        
    Returns:
        bytearray: Modified ROM buffer
    """
    print("Applying autoheal maintenance patch...")
    
    # Create a copy of the ROM data to modify
    patched_rom = bytearray(rom_data)
    
    # The autoheal disable happens in map 0129's script
    # We need to find where [07EF] is being set to 0
    # This is typically done with a STZ (Store Zero) instruction
    
    # Common patterns to look for:
    # STZ $07EF (9C EF 07) - Store zero to absolute address
    # LDA #$00 / STA $07EF (A9 00 8D EF 07) - Load zero and store
    # SEP #$20 / STZ $07EF (E2 20 9C EF 07) - Set 8-bit mode then store zero
    
    patches_applied = 0
    
    # Pattern 1: STZ $07EF
    stz_pattern = bytes([0x9C, 0xEF, 0x07])
    
    # Pattern 2: LDA #$00 / STA $07EF
    lda_sta_pattern = bytes([0xA9, 0x00, 0x8D, 0xEF, 0x07])
    
    # Pattern 3: SEP #$20 / STZ $07EF
    sep_stz_pattern = bytes([0xE2, 0x20, 0x9C, 0xEF, 0x07])
    
    # Pattern 4: LDA #$0000 / STA $07EF (16-bit mode)
    lda16_sta_pattern = bytes([0xA9, 0x00, 0x00, 0x8D, 0xEF, 0x07])
    
    # Search the entire ROM for these patterns
    print("Searching entire ROM for autoheal disable patterns...")
    
    # Search for STZ pattern
    for offset in range(0, len(patched_rom) - 3):
        if patched_rom[offset:offset+3] == stz_pattern:
            print(f"Found STZ $07EF at offset {hex(offset)} (bank ${offset//0x8000:02X})")
            # Replace with NOP instructions (EA)
            patched_rom[offset] = 0xEA     # NOP
            patched_rom[offset+1] = 0xEA   # NOP
            patched_rom[offset+2] = 0xEA   # NOP
            patches_applied += 1
            print(f"[OK] Patched STZ $07EF at {hex(offset)} with NOPs")
    
    # Search for LDA/STA pattern
    for offset in range(0, len(patched_rom) - 5):
        if patched_rom[offset:offset+5] == lda_sta_pattern:
            print(f"Found LDA #$00 / STA $07EF at offset {hex(offset)} (bank ${offset//0x8000:02X})")
            # Replace with NOP instructions
            for i in range(5):
                patched_rom[offset+i] = 0xEA  # NOP
            patches_applied += 1
            print(f"[OK] Patched LDA/STA sequence at {hex(offset)} with NOPs")
    
    # Search for SEP/STZ pattern
    for offset in range(0, len(patched_rom) - 5):
        if patched_rom[offset:offset+5] == sep_stz_pattern:
            print(f"Found SEP #$20 / STZ $07EF at offset {hex(offset)} (bank ${offset//0x8000:02X})")
            # Keep SEP but NOP the STZ
            patched_rom[offset+2] = 0xEA   # NOP
            patched_rom[offset+3] = 0xEA   # NOP
            patched_rom[offset+4] = 0xEA   # NOP
            patches_applied += 1
            print(f"[OK] Patched SEP/STZ sequence at {hex(offset)}")
    
    # Search for 16-bit LDA/STA pattern
    for offset in range(0, len(patched_rom) - 6):
        if patched_rom[offset:offset+6] == lda16_sta_pattern:
            print(f"Found LDA #$0000 / STA $07EF at offset {hex(offset)} (bank ${offset//0x8000:02X})")
            # Replace with NOP instructions
            for i in range(6):
                patched_rom[offset+i] = 0xEA  # NOP
            patches_applied += 1
            print(f"[OK] Patched 16-bit LDA/STA sequence at {hex(offset)} with NOPs")
    
    # Also search for indirect patterns that might set 07EF
    # Sometimes the game uses indexed addressing or other methods
    
    # Pattern 5: STA $07EF,X or STA $07EF,Y (where X/Y = 0)
    sta_indexed_patterns = [
        bytes([0x9D, 0xEF, 0x07]),  # STA $07EF,X
        bytes([0x99, 0xEF, 0x07]),  # STA $07EF,Y
    ]
    
    for pattern in sta_indexed_patterns:
        for offset in range(0, len(patched_rom) - 3):
            if patched_rom[offset:offset+3] == pattern:
                # Check if this might be clearing the value
                # Look back a few bytes to see if A register is being set to 0
                if offset >= 2 and patched_rom[offset-2] == 0xA9 and patched_rom[offset-1] == 0x00:
                    print(f"Found indexed STA $07EF at offset {hex(offset)} with A=0")
                    # NOP out both the LDA and STA
                    for i in range(-2, 3):
                        patched_rom[offset+i] = 0xEA
                    patches_applied += 1
                    print(f"[OK] Patched indexed store at {hex(offset)}")
    
    if patches_applied == 0:
        print("[WARN] No autoheal disable instructions found!")
        print("Applying alternative patch method...")
        
        # Alternative: Hook the chapter 2 transition and force autoheal on
        # We'll look for specific map transitions or events
        
        # Try to find map 0129 loading code and insert our patch there
        # Map IDs are usually loaded with LDA #$29 / STA somewhere
        map_load_pattern = bytes([0xA9, 0x29, 0x01])  # LDA #$0129
        
        for offset in range(0, len(patched_rom) - 3):
            if patched_rom[offset:offset+3] == map_load_pattern:
                print(f"Found map 0129 load at offset {hex(offset)}")
                # Look for nearby free space to insert our patch
                # We'll look for a series of 0xFF bytes (common in unused space)
                
                for search_offset in range(offset + 0x100, min(offset + 0x1000, len(patched_rom) - 10)):
                    if all(patched_rom[search_offset+i] == 0xFF for i in range(10)):
                        print(f"Found free space at {hex(search_offset)}")
                        
                        # Insert our autoheal enable code
                        code_offset = search_offset
                        # LDA #$01
                        patched_rom[code_offset] = 0xA9
                        patched_rom[code_offset+1] = 0x01
                        # STA $07EF
                        patched_rom[code_offset+2] = 0x8D
                        patched_rom[code_offset+3] = 0xEF
                        patched_rom[code_offset+4] = 0x07
                        # RTS or RTL depending on context
                        patched_rom[code_offset+5] = 0x60  # RTS
                        
                        patches_applied = 1
                        print(f"[OK] Inserted autoheal enable routine at {hex(code_offset)}")
                        break
                
                if patches_applied > 0:
                    break
    
    print(f"\nAutoheal patch completed: {patches_applied} patches applied")
    
    if patches_applied == 0:
        print("[ERROR] Could not apply autoheal patch - no suitable locations found")
        print("The ROM may have a different structure than expected")
    
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
    
    # Apply autoheal patch if enabled
    if options.get("maintain_autoheal"):
        patched_rom = apply_autoheal_patch(patched_rom)
    
    # Add more patches here as they are developed
    
    return patched_rom

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
            # Apply autoheal patch if enabled
    if options.get("maintain_autoheal"):
        patched_rom = apply_autoheal_patch(patched_rom)
    
    # Add more patches here as they are developed
    
    return patched_rom