#!/usr/bin/env python3
"""
GUI for Terranigma Randomizer
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import sys
import subprocess
import threading
import json
from pathlib import Path

class TerranigmaRandomizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Terranigma Randomizer")
        self.root.geometry("800x600")
        
        # Variables
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.seed = tk.StringVar()
        self.skip_chests = tk.BooleanVar(value=False)
        self.skip_shops = tk.BooleanVar(value=False)
        self.no_logic = tk.BooleanVar(value=False)
        self.scale_equipment = tk.BooleanVar(value=False)
        self.include_accessories = tk.BooleanVar(value=False)
        self.price_variation = tk.IntVar(value=50)
        self.shop_logic = tk.BooleanVar(value=True)
        self.unique_items = tk.BooleanVar(value=True)
        self.items_amount = tk.StringVar(value="normal")
        self.enable_boss_magic = tk.BooleanVar(value=False)
        self.enable_intro_skip = tk.BooleanVar(value=False)
        self.status_var = tk.StringVar(value="Ready")
        
        # Create widgets
        self.create_widgets()
        
        # Center window
        self.center_window()
        
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
    def create_widgets(self):
        """Create all GUI widgets"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # File selection frame
        file_frame = ttk.LabelFrame(main_frame, text="ROM Files", padding="10")
        file_frame.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        file_frame.columnconfigure(1, weight=1)
        
        # Input ROM
        ttk.Label(file_frame, text="Input ROM:").grid(row=0, column=0, sticky=tk.W, padx=5)
        ttk.Entry(file_frame, textvariable=self.input_path).grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(file_frame, text="Browse...", command=self.browse_input).grid(row=0, column=2, padx=5)
        
        # Output ROM
        ttk.Label(file_frame, text="Output ROM:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(file_frame, textvariable=self.output_path).grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        ttk.Button(file_frame, text="Browse...", command=self.browse_output).grid(row=1, column=2, padx=5, pady=5)
        
        # Options notebook (tabs)
        notebook = ttk.Notebook(main_frame)
        notebook.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        # Basic tab
        basic_tab = ttk.Frame(notebook, padding="10")
        notebook.add(basic_tab, text="Basic Options")
        
        # Advanced tab
        advanced_tab = ttk.Frame(notebook, padding="10")
        notebook.add(advanced_tab, text="Advanced Options")
        
        # ASM Patches tab
        asm_tab = ttk.Frame(notebook, padding="10")
        notebook.add(asm_tab, text="ASM Patches")
        
        # Basic Tab Content
        basic_tab.columnconfigure(1, weight=1)
        
        # Seed
        ttk.Label(basic_tab, text="Seed (optional):").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        seed_entry = ttk.Entry(basic_tab, textvariable=self.seed, width=20)
        seed_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        
        # Checkboxes for basic options
        ttk.Checkbutton(basic_tab, text="Skip chest randomization", variable=self.skip_chests).grid(
            column=0, row=1, columnspan=2, sticky=tk.W, padx=5, pady=5)
        ttk.Checkbutton(basic_tab, text="Skip shop randomization", variable=self.skip_shops).grid(
            column=0, row=2, columnspan=2, sticky=tk.W, padx=5, pady=5)
        ttk.Checkbutton(basic_tab, text="Use purely random placement (no logic)", variable=self.no_logic).grid(
            column=0, row=3, columnspan=2, sticky=tk.W, padx=5, pady=5)
        
        # Warning for no logic
        warning_label = ttk.Label(basic_tab, text="⚠ No logic mode may create unbeatable seeds!", 
                                 foreground="red", font=("", 9, "italic"))
        warning_label.grid(column=0, row=4, columnspan=2, sticky=tk.W, padx=25, pady=0)
        
        # Advanced Tab Content
        advanced_tab.columnconfigure(1, weight=1)
        
        # Shop options
        ttk.Checkbutton(advanced_tab, text="Scale equipment to progression", variable=self.scale_equipment).grid(
            column=0, row=0, columnspan=2, sticky=tk.W, padx=5, pady=5)
        ttk.Checkbutton(advanced_tab, text="Include accessories in shops", variable=self.include_accessories).grid(
            column=0, row=1, columnspan=2, sticky=tk.W, padx=5, pady=5)
        
        # Price variation
        ttk.Label(advanced_tab, text="Price variation %:").grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        price_scale = ttk.Scale(advanced_tab, from_=0, to=100, variable=self.price_variation, orient=tk.HORIZONTAL)
        price_scale.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=5, pady=5)
        price_label = ttk.Label(advanced_tab, textvariable=self.price_variation)
        price_label.grid(column=2, row=2, padx=5, pady=5)
        
        # Logic options
        logic_frame = ttk.LabelFrame(advanced_tab, text="Logic Options", padding=10)
        logic_frame.grid(column=0, row=5, columnspan=3, sticky="ew", padx=5, pady=10)
        
        ttk.Checkbutton(logic_frame, text="Integrate shops into progression logic", variable=self.shop_logic).pack(anchor=tk.W, padx=5, pady=2)
        ttk.Checkbutton(logic_frame, text="Enforce unique weapons/armor", variable=self.unique_items).pack(anchor=tk.W, padx=5, pady=2)
        
        # Shop item quantity - using a more compact radio button group
        item_frame = ttk.LabelFrame(advanced_tab, text="Shop Item Quantity", padding=10)
        item_frame.grid(column=0, row=3, columnspan=3, sticky="ew", padx=5, pady=10)
        
        self.items_amount = tk.StringVar(value="normal")
        ttk.Radiobutton(item_frame, text="Normal", variable=self.items_amount, value="normal").pack(anchor=tk.W, padx=5, pady=2)
        ttk.Radiobutton(item_frame, text="More items", variable=self.items_amount, value="more").pack(anchor=tk.W, padx=5, pady=2)
        ttk.Radiobutton(item_frame, text="Fewer items", variable=self.items_amount, value="fewer").pack(anchor=tk.W, padx=5, pady=2)
        
        # ASM Patches Tab Content
        asm_tab.columnconfigure(0, weight=1)
        
        # Frame for gameplay patches
        gameplay_frame = ttk.LabelFrame(asm_tab, text="Gameplay Modifications", padding=10)
        gameplay_frame.grid(column=0, row=0, sticky="ew", padx=5, pady=10)
        
        # Boss magic checkbox
        self.enable_boss_magic = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            gameplay_frame, 
            text="Enable magic in boss fights (allows magic usage in all boss battles)", 
            variable=self.enable_boss_magic
        ).pack(anchor=tk.W, padx=5, pady=5)
        
        # Intro skip checkbox
        self.skip_intro = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            gameplay_frame, 
            text="Skip intro (start with necessary flags and items)", 
            variable=self.skip_intro
        ).pack(anchor=tk.W, padx=5, pady=5)
        
        # Room for additional ASM patches in the future
        # Just add more checkboxes or options here as needed
        
        # Randomize Button - placed right after the tabs
        randomize_button = ttk.Button(main_frame, text="Randomize!", command=self.randomize_thread, style='Accent.TButton')
        randomize_button.grid(row=2, column=0, columnspan=3, pady=10)
        
        # Status bar
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        status_frame.columnconfigure(0, weight=1)
        
        ttk.Label(status_frame, text="Status:").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(status_frame, textvariable=self.status_var).grid(row=0, column=1, sticky=tk.W, padx=5)
        
        # Output text area
        output_frame = ttk.LabelFrame(main_frame, text="Output", padding="5")
        output_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=10, wrap=tk.WORD)
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
    def browse_input(self):
        """Browse for input ROM file"""
        filename = filedialog.askopenfilename(
            title="Select Terranigma ROM",
            filetypes=[("SNES ROM files", "*.sfc *.smc"), ("All files", "*.*")]
        )
        if filename:
            self.input_path.set(filename)
            # Auto-generate output path
            path = Path(filename)
            output_name = f"{path.stem}_randomized{path.suffix}"
            self.output_path.set(str(path.parent / output_name))
            
    def browse_output(self):
        """Browse for output ROM file"""
        filename = filedialog.asksaveasfilename(
            title="Save Randomized ROM As",
            defaultextension=".sfc",
            filetypes=[("SNES ROM files", "*.sfc *.smc"), ("All files", "*.*")]
        )
        if filename:
            self.output_path.set(filename)
            
    def randomize_thread(self):
        """Run randomizer in a separate thread"""
        thread = threading.Thread(target=self.run_randomizer)
        thread.daemon = True
        thread.start()
        
    def get_executable_path(self):
        """Get the path to the CLI randomizer executable"""
        if getattr(sys, 'frozen', False):
            # Running as compiled executable
            base_path = sys._MEIPASS
        else:
            # Running as script
            base_path = os.path.dirname(os.path.abspath(__file__))
            
        # Look for the CLI executable
        if sys.platform == "win32":
            exe_name = "terranigma-randomizer.exe"
        else:
            exe_name = "terranigma-randomizer"
            
        # Check in the same directory first
        exe_path = os.path.join(os.path.dirname(base_path), exe_name)
        if os.path.exists(exe_path):
            return exe_path
            
        # Check in Scripts directory (for pip installs)
        scripts_path = os.path.join(sys.prefix, "Scripts" if sys.platform == "win32" else "bin", exe_name)
        if os.path.exists(scripts_path):
            return scripts_path
            
        # Fallback to just the executable name and hope it's in PATH
        return exe_name
        
    def run_randomizer(self):
        """Run the randomizer with the current settings"""
        # Clear output
        self.output_text.delete(1.0, tk.END)
        
        # Validate inputs
        if not self.input_path.get():
            self.output_text.insert(tk.END, "Error: Input ROM path not specified.\n")
            self.status_var.set("Error: Input ROM not specified")
            return
            
        if not self.output_path.get():
            self.output_text.insert(tk.END, "Error: Output ROM path not specified.\n")
            self.status_var.set("Error: Output ROM not specified")
            return
        
        # Get the path to the CLI randomizer executable
        randomizer_exe = self.get_executable_path()
        
        # Add verification that the input ROM exists
        if not os.path.exists(self.input_path.get()):
            self.output_text.insert(tk.END, f"Error: Input ROM file not found: {self.input_path.get()}\n")
            self.status_var.set("Error: Input ROM not found")
            return
        
        # Update status
        self.status_var.set("Randomizing...")
        
        # Build command
        cmd = [randomizer_exe, self.input_path.get(), self.output_path.get()]
        
        # Add optional parameters
        if self.seed.get():
            cmd.extend(["--seed", self.seed.get()])
        
        if self.skip_chests.get():
            cmd.append("--skip-chests")
        
        if self.skip_shops.get():
            cmd.append("--skip-shops")
        
        if self.no_logic.get():
            cmd.append("--no-logic")
        
        if self.scale_equipment.get():
            cmd.append("--scale-equipment")
        
        if self.include_accessories.get():
            cmd.append("--include-accessories")
        
        if self.items_amount.get() == "more":
            cmd.append("--more-items")
        elif self.items_amount.get() == "fewer":
            cmd.append("--fewer-items")
        
        cmd.extend(["--price-variation", str(self.price_variation.get())])
        
        if not self.shop_logic.get():
            cmd.append("--no-integrate-shop-logic")
        
        if not self.unique_items.get():
            cmd.append("--allow-duplicates")
            
        # Add ASM patch options
        if self.enable_boss_magic.get():
            cmd.append("--enable-boss-magic")
        
        if self.skip_intro.get():
            cmd.append("--skip-intro")
        
        self.output_text.insert(tk.END, f"Using randomizer: {randomizer_exe}\n")
        self.output_text.insert(tk.END, f"Checking if randomizer exists: {os.path.exists(randomizer_exe)}\n")
        self.output_text.insert(tk.END, f"Running command: {' '.join(cmd)}\n\n")
        
        # Run the randomizer
        try:
            # Use direct import if the executable doesn't exist
            if not os.path.exists(randomizer_exe):
                self.output_text.insert(tk.END, "CLI randomizer not found, using direct import...\n")
                # Import and run directly
                from terranigma_randomizer.__main__ import run_randomizer
                
                # Parse seed
                seed = None
                if self.seed.get():
                    try:
                        seed = int(self.seed.get())
                    except ValueError:
                        self.output_text.insert(tk.END, f"Warning: Invalid seed '{self.seed.get()}', using random seed\n")
                
                # Build options dict
                options = {
                    "seed": seed if seed is not None else None,
                    "randomize_chests": not self.skip_chests.get(),
                    "randomize_shops": not self.skip_shops.get(),
                    "use_logic": not self.no_logic.get(),
                    "verbose": False,
                    "max_attempts": 5000,
                    "integrate_shop_logic": self.shop_logic.get(),
                    "enforce_unique_items": self.unique_items.get(),
                    "randomize_items": True,
                    "keep_consumables_in_shops": True,
                    "keep_item_types": True,
                    "scale_equipment": self.scale_equipment.get(),
                    "randomize_prices": True,
                    "price_variation": self.price_variation.get(),
                    "items_per_shop": self.items_amount.get(),
                    "include_accessories": self.include_accessories.get(),
                    "include_key_items": False,
                    "special_items": [],
                    "enable_boss_magic": self.enable_boss_magic.get(),
                    "skip_intro": self.skip_intro.get(),
                }
                
                # Run randomizer
                result = run_randomizer(self.input_path.get(), self.output_path.get(), options)
                
                if result["success"]:
                    self.output_text.insert(tk.END, f"\n{result['message']}\n")
                    self.status_var.set("Randomization complete!")
                    messagebox.showinfo("Success", result["message"])
                else:
                    self.output_text.insert(tk.END, f"\n{result['error']}\n")
                    self.status_var.set("Randomization failed!")
                    messagebox.showerror("Error", result["error"])
                    
            else:
                # Run as subprocess
                process = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    universal_newlines=True
                )
                
                # Read output line by line
                for line in process.stdout:
                    self.output_text.insert(tk.END, line)
                    self.output_text.see(tk.END)
                    self.output_text.update()
                
                # Wait for completion
                return_code = process.wait()
                
                if return_code == 0:
                    self.status_var.set("Randomization complete!")
                    messagebox.showinfo("Success", "Randomization completed successfully!")
                else:
                    self.status_var.set("Randomization failed!")
                    messagebox.showerror("Error", f"Randomization failed with code {return_code}")
                    
        except Exception as e:
            error_msg = f"Error running randomizer: {str(e)}"
            self.output_text.insert(tk.END, f"\n{error_msg}\n")
            self.status_var.set("Error!")
            messagebox.showerror("Error", error_msg)

def main():
    """Main entry point for the GUI"""
    root = tk.Tk()
    app = TerranigmaRandomizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()