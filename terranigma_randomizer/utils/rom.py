"""
ROM reading and writing utilities for Terranigma Randomizer
"""

def read_rom(filepath):
    """
    Read ROM data from a file
    
    Args:
        filepath (str): Path to the ROM file
        
    Returns:
        bytearray: ROM data
    """
    with open(filepath, 'rb') as f:
        return bytearray(f.read())

def write_rom(filepath, data):
    """
    Write ROM data to a file
    
    Args:
        filepath (str): Path to the output ROM file
        data (bytearray): ROM data to write
        
    Returns:
        bool: True if successful
    """
    with open(filepath, 'wb') as f:
        f.write(data)
    return True

def read_byte(rom_data, address):
    """
    Read a single byte from ROM
    
    Args:
        rom_data (bytearray): ROM data
        address (int): Address to read from
        
    Returns:
        int: Byte value
    """
    return rom_data[address]

def read_word(rom_data, address):
    """
    Read a 16-bit word from ROM
    
    Args:
        rom_data (bytearray): ROM data
        address (int): Address to read from
        
    Returns:
        int: 16-bit word value
    """
    return rom_data[address] | (rom_data[address + 1] << 8)

def write_byte(rom_data, address, value):
    """
    Write a single byte to ROM
    
    Args:
        rom_data (bytearray): ROM data
        address (int): Address to write to
        value (int): Byte value to write
        
    Returns:
        None
    """
    rom_data[address] = value & 0xFF

def write_word(rom_data, address, value):
    """
    Write a 16-bit word to ROM
    
    Args:
        rom_data (bytearray): ROM data
        address (int): Address to write to
        value (int): 16-bit word value to write
        
    Returns:
        None
    """
    rom_data[address] = value & 0xFF
    rom_data[address + 1] = (value >> 8) & 0xFF
