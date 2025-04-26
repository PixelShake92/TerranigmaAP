# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['gui.py'],
    pathex=['.', './terranigma_randomizer', './terranigma_randomizer/randomizers', './terranigma_randomizer/utils', './terranigma_randomizer/constants'],
    binaries=[],
    datas=[],
    hiddenimports=['terranigma_randomizer.randomizers.chest', 'terranigma_randomizer.randomizers.shop', 'terranigma_randomizer.randomizers.integration', 'terranigma_randomizer.utils.rom', 'terranigma_randomizer.utils.logic', 'terranigma_randomizer.utils.spoilers', 'terranigma_randomizer.utils.asm', 'terranigma_randomizer.constants.items', 'terranigma_randomizer.constants.chests', 'terranigma_randomizer.constants.shops', 'terranigma_randomizer.constants.progression', 'tkinter', 'tkinter.filedialog', 'tkinter.ttk'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='terranigma-randomizer-gui',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
