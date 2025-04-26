#!/usr/bin/env python3
"""
Build script for Terranigma Randomizer
Handles the entire build process from start to finish
"""
import os
import sys
import subprocess
import shutil

def create_init_files():
    """Create __init__.py files in all module directories"""
    directories = [
        'terranigma_randomizer',
        'terranigma_randomizer/randomizers',
        'terranigma_randomizer/utils',
        'terranigma_randomizer/constants'
    ]
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory {directory}")
        
        init_file = os.path.join(directory, '__init__.py')
        if not os.path.exists(init_file):
            try:
                with open(init_file, 'w') as f:
                    f.write('# Auto-generated __init__.py file\n')
                print(f"Created {init_file}")
            except Exception as e:
                print(f"Error creating {init_file}: {e}")

def build_executable():
    """Build the executable using PyInstaller"""
    print("\n=== Building Terranigma Randomizer Executable ===\n")
    
    # Step 1: Create __init__.py files
    print("Step 1: Creating __init__.py files...")
    create_init_files()
    
    # Step 2: Run PyInstaller with the spec file
    print("\nStep 2: Running PyInstaller...")
    result = subprocess.run(['pyinstaller', '--clean', 'terranigma-randomizer.spec'], 
                           capture_output=True, text=True)
    
    if result.returncode != 0:
        print("PyInstaller failed with the following error:")
        print(result.stderr)
        print("\nTrying alternative build method...")
        
        # Alternative build method
        result = subprocess.run([
            'pyinstaller',
            '--onefile',
            '--name=terranigma-randomizer',
            '--paths=.',
            '--paths=./terranigma_randomizer',
            '--paths=./terranigma_randomizer/randomizers',
            '--paths=./terranigma_randomizer/utils',
            '--paths=./terranigma_randomizer/constants',
            '--hidden-import=terranigma_randomizer.randomizers.chest',
            '--hidden-import=terranigma_randomizer.randomizers.shop',
            '--hidden-import=terranigma_randomizer.randomizers.integration',
            '--hidden-import=terranigma_randomizer.utils.rom',
            '--hidden-import=terranigma_randomizer.utils.logic', 
            '--hidden-import=terranigma_randomizer.utils.spoilers',
            '--hidden-import=terranigma_randomizer.constants.items',
            '--hidden-import=terranigma_randomizer.constants.chests',
            '--hidden-import=terranigma_randomizer.constants.shops',
            '--hidden-import=terranigma_randomizer.constants.progression',
            'terranigma_randomizer/__main__.py'
        ], capture_output=True, text=True)
        
        if result.returncode != 0:
            print("Alternative build method also failed:")
            print(result.stderr)
            return False
    
    # Step 3: Build the GUI version
    print("\nStep 3: Building GUI version...")
    result_gui = subprocess.run([
        'pyinstaller',
        '--onefile',
        '--windowed',  # This creates a GUI app without console window
        '--name=terranigma-randomizer-gui',
        '--paths=.',
        '--paths=./terranigma_randomizer',
        '--paths=./terranigma_randomizer/randomizers',
        '--paths=./terranigma_randomizer/utils',
        '--paths=./terranigma_randomizer/constants',
        '--hidden-import=terranigma_randomizer.randomizers.chest',
        '--hidden-import=terranigma_randomizer.randomizers.shop',
        '--hidden-import=terranigma_randomizer.randomizers.integration',
        '--hidden-import=terranigma_randomizer.utils.rom',
        '--hidden-import=terranigma_randomizer.utils.logic',
        '--hidden-import=terranigma_randomizer.utils.spoilers',
        '--hidden-import=terranigma_randomizer.constants.items',
        '--hidden-import=terranigma_randomizer.constants.chests',
        '--hidden-import=terranigma_randomizer.constants.shops',
        '--hidden-import=terranigma_randomizer.constants.progression',
        '--hidden-import=tkinter',
        '--hidden-import=tkinter.filedialog',
        '--hidden-import=tkinter.ttk',
        'gui.py'
    ], capture_output=True, text=True)
    
    if result_gui.returncode != 0:
        print("GUI build failed with the following error:")
        print(result_gui.stderr)
    else:
        print("GUI build successful!")
    
    # Step 4: Create CLI copy to avoid confusion
    cli_exe = os.path.join('dist', 'terranigma-randomizer.exe')
    cli_copy = os.path.join('dist', 'terranigma-randomizer-cli.exe')
    if os.path.exists(cli_exe):
        try:
            shutil.copy(cli_exe, cli_copy)
            print(f"Created CLI copy at: {cli_copy}")
        except Exception as e:
            print(f"Failed to create CLI copy: {e}")
    
    # Step 5: Verify the builds
    exe_path = os.path.join('dist', 'terranigma-randomizer.exe')
    gui_path = os.path.join('dist', 'terranigma-randomizer-gui.exe')
    
    success = False
    
    if os.path.exists(exe_path):
        print(f"\nCLI build successful! Executable created at: {exe_path}")
        success = True
    else:
        print("\nCLI build process completed, but executable was not found.")
    
    if os.path.exists(gui_path):
        print(f"GUI build successful! Executable created at: {gui_path}")
        success = True
    
    return success

if __name__ == "__main__":
    success = build_executable()
    sys.exit(0 if success else 1)