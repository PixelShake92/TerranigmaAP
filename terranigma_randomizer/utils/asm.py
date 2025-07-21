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

def apply_intro_skip_patch(rom_data):
    """
    Apply intro skip patch - direct translation of the ASAR patch:
    
    This patch:
    1. Hooks the intro at $90886f to jump to custom code at $FE0000
    2. Sets all necessary starting flags for the game
    3. Sets flag to open the gate (using LDA #$5F instead of #$1F)
    4. Opens Tower 1 doors (sets $0710 to #$0F)
    5. Sets starting level to 3 (EXP values at $0690-$0691)
    6. Sets starting gems to 1000 (BCD format at $0694-$0696)
    7. Opens access to all towers (sets $06E0 to #$AB)
    8. Enables Crystal Thread sequence (sets $06E3 to #$34)
    9. Sets initial inventory items (Jewel Box, CrySpear, Clothes)
    10. Warps the player outside Crysta (coordinates: $0003, $00, $55, $0210, $0210)
    
    Args:
        rom_data (bytearray): ROM buffer
        
    Returns:
        bytearray: Modified ROM buffer
    """
    print("Applying intro skip patch...")
    print(f"ROM size: {len(rom_data)} bytes ({hex(len(rom_data))})")
    
    # Create a copy of the ROM data to modify
    patched_rom = bytearray(rom_data)
    
    # org $90886f - Hook location (HiROM address)
    # In HiROM: Bank $90 mirrors bank $10
    # $90886F = ROM offset $10886F
    hook_offset = 0x10886F
    
    # First, let's see what's currently at the hook location
    print(f"\nBefore patching at hook location ${hook_offset:06X}:")
    debug_rom_section(patched_rom, hook_offset, 16)
    
    # JML $FE0000
    patched_rom[hook_offset + 0] = 0x5C  # JML opcode
    patched_rom[hook_offset + 1] = 0x00
    patched_rom[hook_offset + 2] = 0x00
    patched_rom[hook_offset + 3] = 0xFE
    
    # NOP #6
    for i in range(6):
        patched_rom[hook_offset + 4 + i] = 0xEA
    
    print(f"\nAfter patching at hook location ${hook_offset:06X}:")
    debug_rom_section(patched_rom, hook_offset, 16)
    
    # org $FE0000 - Custom code location (HiROM address)
    # In HiROM: $FE0000 = ROM offset $3E0000
    code_offset = 0x3E0000
    
    # Check if we have enough space
    if code_offset >= len(patched_rom):
        print(f"ERROR: Code offset ${code_offset:06X} is beyond ROM size!")
        print(f"ROM size is only ${len(patched_rom):06X}")
        return patched_rom
    
    print(f"\nBefore patching at code location ${code_offset:06X}:")
    debug_rom_section(patched_rom, code_offset, 32)
    
    # The full patch code exactly as in my current ASM
    code_bytes = [
        # SEP #$20
        0xE2, 0x20,
        
        # LDA #$CF
        0xA9, 0xCF,
        # ORA $06C4
        0x0D, 0xC4, 0x06,
        # STA $06C4
        0x8D, 0xC4, 0x06,
        
        # LDA #$43  (changed from #$41 to set post-Crystal Thread state)
        0xA9, 0x43,
        # ORA $06C5
        0x0D, 0xC5, 0x06,
        # STA $06C5
        0x8D, 0xC5, 0x06,
        
        # LDA #$10
        0xA9, 0x10,
        # ORA $06C7
        0x0D, 0xC7, 0x06,
        # STA $06C7
        0x8D, 0xC7, 0x06,
        
        # LDA #$40
        0xA9, 0x40,
        # ORA $06DF
        0x0D, 0xDF, 0x06,
        # STA $06DF
        0x8D, 0xDF, 0x06,
        
        # LDA #$1F
        0xA9, 0x1F,
        # ORA $0708
        0x0D, 0x08, 0x07,
        # STA $0708
        0x8D, 0x08, 0x07,
        
        # LDA #$5F  (changed from #$1F to open the gate)
        0xA9, 0x5F,
        # ORA $0712
        0x0D, 0x12, 0x07,
        # STA $0712
        0x8D, 0x12, 0x07,
        
        # LDA #$0F
        0xA9, 0x0F,
        # STA $0710 (open Tower 1 doors)
        0x8D, 0x10, 0x07,
        
        # Set level 3
        # LDA #$20
        0xA9, 0x20,
        # STA $0690 (Level/EXP byte 0)
        0x8D, 0x90, 0x06,
        # LDA #$01
        0xA9, 0x01,
        # STA $0691 (Level/EXP byte 1)
        0x8D, 0x91, 0x06,
        
        # Set 1000 gems (BCD format)
        # LDA #$00
        0xA9, 0x00,
        # STA $0694 (Gems byte 0)
        0x8D, 0x94, 0x06,
        # LDA #$10
        0xA9, 0x10,
        # STA $0695 (Gems byte 1 - 1000 in BCD)
        0x8D, 0x95, 0x06,
        # LDA #$00
        0xA9, 0x00,
        # STA $0696 (Gems byte 2)
        0x8D, 0x96, 0x06,
        
        # Open access to all towers
        # LDA #$AB
        0xA9, 0xAB,
        # STA $06E0 (Tower access flags)
        0x8D, 0xE0, 0x06,
        
        # Enable Crystal Thread sequence
        # LDA #$34
        0xA9, 0x34,
        # STA $06E3 (Crystal Thread sequence flag)
        0x8D, 0xE3, 0x06,
        
        # REP #$20
        0xC2, 0x20,
        
        # LDA #$017A
        0xA9, 0x7A, 0x01,
        # STA $7F8036
        0x8F, 0x36, 0x80, 0x7F,
        
        # LDA #$0181
        0xA9, 0x81, 0x01,
        # STA $7F8048
        0x8F, 0x48, 0x80, 0x7F,
        
        # LDA #$01A0
        0xA9, 0xA0, 0x01,
        # STA $7F8068
        0x8F, 0x68, 0x80, 0x7F,
        
        # COP #$14
        0x02, 0x14,
        # dw $0003  (Exit Crysta)
        0x03, 0x00,
        # db $00
        0x00,
        # db $55
        0x55,
        # dw $0210
        0x10, 0x02,
        # dw $0210
        0x10, 0x02,
        
        # JML $908879
        0x5C, 0x79, 0x88, 0x90
    ]
    
    # Write the custom code
    for i, byte in enumerate(code_bytes):
        if code_offset + i < len(patched_rom):
            patched_rom[code_offset + i] = byte
        else:
            print(f"ERROR: Trying to write beyond ROM size at ${code_offset + i:06X}")
            break
    
    print(f"\nAfter patching at code location ${code_offset:06X}:")
    debug_rom_section(patched_rom, code_offset, 32)
    
    print(f"\n[OK] Intro skip patch applied")
    print(f"  - Hook at $90886F (ROM: ${hook_offset:06X})")
    print(f"  - Custom code at $FE0000 (ROM: ${code_offset:06X})")
    
    # Let's also verify the bytes were actually changed
    hook_changed = False
    for i in range(10):
        if rom_data[hook_offset + i] != patched_rom[hook_offset + i]:
            hook_changed = True
            break
    
    code_changed = False
    for i in range(len(code_bytes)):
        if code_offset + i < len(rom_data) and code_offset + i < len(patched_rom):
            if rom_data[code_offset + i] != patched_rom[code_offset + i]:
                code_changed = True
                break
    
    print(f"\nVerification:")
    print(f"  - Hook location modified: {hook_changed}")
    print(f"  - Code location modified: {code_changed}")
    
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
    
    # Apply intro skip patch if enabled
    if options.get("skip_intro", False):
        patched_rom = apply_intro_skip_patch(patched_rom)
    
    # Apply boss magic patch if enabled
    if options.get("enable_boss_magic", False):
        patched_rom = apply_boss_magic_patch(patched_rom)
    
    # Add more patches here as they are developed
    
    return patched_rom