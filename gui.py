import tkinter as tk
from tkinter import filedialog, ttk
import subprocess
import os
import sys
import random

class TerranigmaRandomizerGUI:
    def __init__(self, root):
        self.root = root
        root.title("Terranigma Randomizer")
        
        # Set a larger default size that works well with all content
        root.geometry("700x700")
        root.minsize(650, 600)  # Set minimum window size
        
        # Create a main frame with padding
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configure grid weights to make the layout responsive
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)  # Make output area expandable
        
        # Create tabs for better organization
        tab_control = ttk.Notebook(main_frame)
        tab_control.grid(row=0, column=0, sticky="nsew", pady=(0, 10))
        
        # Basic tab
        basic_tab = ttk.Frame(tab_control, padding=10)
        tab_control.add(basic_tab, text="Basic Options")
        
        # Advanced tab
        advanced_tab = ttk.Frame(tab_control, padding=10)
        tab_control.add(advanced_tab, text="Advanced Options")
        
        # ASM Patches tab
        asm_tab = ttk.Frame(tab_control, padding=10)
        tab_control.add(asm_tab, text="ASM Patches")
        
        # Basic Tab Content
        # Configure grid for basic tab
        basic_tab.columnconfigure(1, weight=1)
        
        # Input/Output File Selection
        ttk.Label(basic_tab, text="Input ROM:").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.input_path = tk.StringVar()
        ttk.Entry(basic_tab, textvariable=self.input_path, width=50).grid(column=1, row=0, sticky="ew", padx=5, pady=5)
        ttk.Button(basic_tab, text="Browse...", command=self.browse_input).grid(column=2, row=0, padx=5, pady=5)
        
        ttk.Label(basic_tab, text="Output ROM:").grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.output_path = tk.StringVar()
        ttk.Entry(basic_tab, textvariable=self.output_path, width=50).grid(column=1, row=1, sticky="ew", padx=5, pady=5)
        ttk.Button(basic_tab, text="Browse...", command=self.browse_output).grid(column=2, row=1, padx=5, pady=5)
        
        # Seed
        ttk.Label(basic_tab, text="Seed (optional):").grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        self.seed = tk.StringVar()
        ttk.Entry(basic_tab, textvariable=self.seed, width=20).grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
        
        # Basic checkboxes
        self.skip_chests = tk.BooleanVar(value=False)
        ttk.Checkbutton(basic_tab, text="Skip chest randomization", variable=self.skip_chests).grid(column=0, row=3, columnspan=3, sticky=tk.W, padx=5, pady=5)
        
        self.skip_shops = tk.BooleanVar(value=False)
        ttk.Checkbutton(basic_tab, text="Skip shop randomization", variable=self.skip_shops).grid(column=0, row=4, columnspan=3, sticky=tk.W, padx=5, pady=5)
        
        self.scale_equipment = tk.BooleanVar(value=False)
        ttk.Checkbutton(basic_tab, text="Scale shop equipment to game progression", variable=self.scale_equipment).grid(column=0, row=5, columnspan=3, sticky=tk.W, padx=5, pady=5)
        
        self.include_accessories = tk.BooleanVar(value=False)
        ttk.Checkbutton(basic_tab, text="Include accessories in shops", variable=self.include_accessories).grid(column=0, row=6, columnspan=3, sticky=tk.W, padx=5, pady=5)
        
        # Price variation slider
        ttk.Label(basic_tab, text="Price variation:").grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
        self.price_variation = tk.IntVar(value=50)
        price_scale = ttk.Scale(basic_tab, from_=0, to=100, variable=self.price_variation, orient=tk.HORIZONTAL)
        price_scale.grid(column=1, row=7, sticky="ew", padx=5, pady=5)
        ttk.Label(basic_tab, textvariable=tk.StringVar(value="50%")).grid(column=2, row=7, padx=5, pady=5)
        price_scale.config(command=lambda val: self.update_price_label(val))
        
        # Advanced Tab Content
        # Configure grid for advanced tab
        advanced_tab.columnconfigure(1, weight=1)
        
        # Detailed logic options
        self.no_logic = tk.BooleanVar(value=False)
        ttk.Checkbutton(advanced_tab, text="Use purely random chest placement (not recommended)", variable=self.no_logic).grid(column=0, row=0, columnspan=3, sticky=tk.W, padx=5, pady=5)
        
        self.shop_logic = tk.BooleanVar(value=True)
        ttk.Checkbutton(advanced_tab, text="Integrate shops into progression logic", variable=self.shop_logic).grid(column=0, row=1, columnspan=3, sticky=tk.W, padx=5, pady=5)
        
        self.unique_items = tk.BooleanVar(value=True)
        ttk.Checkbutton(advanced_tab, text="Ensure weapons and armor appear only once", variable=self.unique_items).grid(column=0, row=2, columnspan=3, sticky=tk.W, padx=5, pady=5)
        
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
        
        # Autoheal maintenance checkbox
        self.maintain_autoheal = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            gameplay_frame,
            text="Maintain autoheal after Chapter 2 (keeps Crystal Spear/Hero Pike healing active)",
            variable=self.maintain_autoheal
        ).pack(anchor=tk.W, padx=5, pady=5)
        
        # Room for additional ASM patches in the future
        # Just add more checkboxes or options here as needed
        
        # Randomize Button - placed right after the tabs
        randomize_button = ttk.Button(main_frame, text="Randomize!", command=self.randomize)
        randomize_button.grid(row=1, column=0, pady=10, sticky="ew")
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=2, column=0, sticky="ew", pady=(0, 5))
        
        # Output area
        output_frame = ttk.LabelFrame(main_frame, text="Output", padding=10)
        output_frame.grid(row=3, column=0, sticky="nsew")
        output_frame.columnconfigure(0, weight=1)
        output_frame.rowconfigure(0, weight=1)
        
        # Create a frame for the text widget and scrollbar
        text_frame = ttk.Frame(output_frame)
        text_frame.grid(row=0, column=0, sticky="nsew")
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(0, weight=1)
        
        self.output_text = tk.Text(text_frame, height=15, width=80, wrap=tk.WORD)
        self.output_text.grid(row=0, column=0, sticky="nsew")
        
        # Add scrollbars
        y_scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.output_text.yview)
        y_scrollbar.grid(row=0, column=1, sticky="ns")
        self.output_text.config(yscrollcommand=y_scrollbar.set)
        
        x_scrollbar = ttk.Scrollbar(text_frame, orient=tk.HORIZONTAL, command=self.output_text.xview)
        x_scrollbar.grid(row=1, column=0, sticky="ew")
        self.output_text.config(xscrollcommand=x_scrollbar.set)
        
    def update_price_label(self, val):
        """Update the price variation label when the slider is moved"""
        try:
            percentage = int(float(val))
            self.root.nametowidget('.!frame.!notebook.!frame.!label4').config(text=f"{percentage}%")
        except (ValueError, KeyError):
            pass
    
    def browse_input(self):
        filename = filedialog.askopenfilename(
            title="Select Input ROM",
            filetypes=(("SNES ROMs", "*.sfc *.smc"), ("All files", "*.*"))
        )
        if filename:
            self.input_path.set(filename)
            
            # Auto-generate output path if empty
            if not self.output_path.get():
                # Add "_randomized" before file extension
                base, ext = os.path.splitext(filename)
                self.output_path.set(f"{base}_randomized{ext}")
    
    def browse_output(self):
        filename = filedialog.asksaveasfilename(
            title="Select Output ROM",
            filetypes=(("SNES ROMs", "*.sfc *.smc"), ("All files", "*.*"))
        )
        if filename:
            self.output_path.set(filename)
    
    def get_executable_path(self):
        """Get the path to the randomizer executable"""
        # Get the directory where the GUI executable is located
        base_dir = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__))
        
        # Look for the CLI randomizer executable in the same directory
        randomizer_exe = os.path.join(base_dir, 'terranigma-randomizer.exe')
        
        if os.path.exists(randomizer_exe):
            return randomizer_exe
        else:
            # If not found, return a path that includes the directory
            return os.path.join(base_dir, 'terranigma-randomizer.exe')
    
    def randomize(self):
        # Clear output area
        self.output_text.delete(1.0, tk.END)
        
        # Check if input and output paths are provided
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
        
        self.output_text.insert(tk.END, f"Using randomizer: {randomizer_exe}\n")
        self.output_text.insert(tk.END, f"Checking if randomizer exists: {os.path.exists(randomizer_exe)}\n")
        self.output_text.insert(tk.END, f"Running command: {' '.join(cmd)}\n\n")
        
        # Run the randomizer
        try:
            # Use direct import if the executable doesn't exist
            if not os.path.exists(randomizer_exe):
                self.output_text.insert(tk.END, "CLI randomizer not found! Using direct import method...\n")
                self.randomize_direct_import()
                return
                
            # Use subprocess.Popen to capture output in real-time
            process = subprocess.Popen(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT, 
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0  # Prevents console window on Windows
            )
            
            # Show output as it comes
            for line in process.stdout:
                self.output_text.insert(tk.END, line)
                self.output_text.see(tk.END)
                self.root.update()
            
            # Wait for process to complete
            process.wait()
            
            if process.returncode == 0:
                self.output_text.insert(tk.END, "\nRandomization completed successfully!\n")
                self.status_var.set("Randomization successful")
                # Verify the output file exists
                if os.path.exists(self.output_path.get()):
                    self.output_text.insert(tk.END, f"Output ROM created at: {self.output_path.get()}\n")
                else:
                    self.output_text.insert(tk.END, f"Warning: Output ROM was not found at: {self.output_path.get()}\n")
            else:
                self.output_text.insert(tk.END, f"\nRandomization failed with code {process.returncode}\n")
                self.status_var.set("Randomization failed")
        
        except Exception as e:
            self.output_text.insert(tk.END, f"Error: {str(e)}\n")
            import traceback
            self.output_text.insert(tk.END, traceback.format_exc())
            self.status_var.set("Error occurred")
    
    def randomize_direct_import(self):
        """Use direct import method for randomization"""
        try:
            # Update status
            self.status_var.set("Randomizing (direct import)...")
            
            # Add parent directory to sys.path for imports
            import sys
            import os
            parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            sys.path.append(parent_dir)
            
            # Import the randomizer function
            from terranigma_randomizer.__main__ import run_randomizer
            
            # Build options dictionary
            options = {
                "seed": int(self.seed.get()) if self.seed.get() else random.randint(0, 999999),
                "randomize_chests": not self.skip_chests.get(),
                "randomize_shops": not self.skip_shops.get(),
                "use_logic": not self.no_logic.get(),
                "verbose": True,
                "max_attempts": 100,
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
                "enable_boss_magic": self.enable_boss_magic.get()
            }
            
            # Capture stdout
            from io import StringIO
            import sys
            original_stdout = sys.stdout
            captured_output = StringIO()
            sys.stdout = captured_output
            
            # Run randomizer
            result = run_randomizer(self.input_path.get(), self.output_path.get(), options)
            
            # Restore stdout
            sys.stdout = original_stdout
            
            # Display output and result
            self.output_text.insert(tk.END, captured_output.getvalue())
            
            if result["success"]:
                self.output_text.insert(tk.END, "\n" + result["message"] + "\n")
                self.status_var.set("Randomization successful")
                # Verify the output file exists
                if os.path.exists(self.output_path.get()):
                    self.output_text.insert(tk.END, f"Output ROM created at: {self.output_path.get()}\n")
                else:
                    self.output_text.insert(tk.END, f"Warning: Output ROM was not found at: {self.output_path.get()}\n")
            else:
                self.output_text.insert(tk.END, "\nError: " + result["error"] + "\n")
                self.status_var.set("Randomization failed")
        
        except Exception as e:
            self.output_text.insert(tk.END, f"Error in direct import method: {str(e)}\n")
            import traceback
            self.output_text.insert(tk.END, traceback.format_exc())
            self.status_var.set("Error occurred")

def main():
    root = tk.Tk()
    app = TerranigmaRandomizerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()