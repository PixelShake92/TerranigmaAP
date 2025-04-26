# -*- mode: python ; coding: utf-8 -*-

import os
import sys

# Get the current directory
current_dir = os.path.abspath(os.path.dirname('__file__'))

# Define paths to important modules
randomizers_dir = os.path.join(current_dir, 'terranigma_randomizer', 'randomizers')
utils_dir = os.path.join(current_dir, 'terranigma_randomizer', 'utils')
constants_dir = os.path.join(current_dir, 'terranigma_randomizer', 'constants')

# Create a block that explains our imports
block_cipher = None

# Define data files to include
datas = [
    (os.path.join(randomizers_dir, '*.py'), 'terranigma_randomizer/randomizers'),
    (os.path.join(utils_dir, '*.py'), 'terranigma_randomizer/utils'),
    (os.path.join(constants_dir, '*.py'), 'terranigma_randomizer/constants'),
]

a = Analysis(
    ['terranigma_randomizer/__main__.py'],
    pathex=[current_dir, randomizers_dir, utils_dir, constants_dir],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'terranigma_randomizer.randomizers.chest', 
        'terranigma_randomizer.randomizers.shop', 
        'terranigma_randomizer.randomizers.integration',
        'terranigma_randomizer.utils.rom',
        'terranigma_randomizer.utils.logic',
        'terranigma_randomizer.utils.spoilers',
        'terranigma_randomizer.constants.items',
        'terranigma_randomizer.constants.chests',
        'terranigma_randomizer.constants.shops',
        'terranigma_randomizer.constants.progression'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='terranigma-randomizer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)