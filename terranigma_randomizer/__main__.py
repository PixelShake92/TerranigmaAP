#!/usr/bin/env python3
"""
Terranigma Randomizer
Main entry point for the randomizer
"""
import argparse
import os
import sys
import random
from pathlib import Path

# Import modules properly
from terranigma_randomizer.randomizers import chest, shop, integration
from terranigma_randomizer.utils import rom, logic, spoilers, asm
from terranigma_randomizer.constants import items, progression

def main():
    """Main entry point for the randomizer CLI"""
    parser = argparse.ArgumentParser(description="Terranigma Randomizer")
    parser.add_argument("input_rom", help="Path to the input ROM file")
    parser.add_argument("output_rom", help="Path to the output ROM file")
    parser.add_argument("--seed", type=int, help="Random seed (default: random)")
    parser.add_argument("--skip-chests", action="store_true", help="Skip chest randomization")
    parser.add_argument("--skip-shops", action="store_true", help="Skip shop randomization")
    parser.add_argument("--no-logic", action="store_true", help="Use purely random chest placement (not recommended)")
    parser.add_argument("--scale-equipment", action="store_true", help="Scale shop equipment to game progression")
    parser.add_argument("--include-accessories", action="store_true", help="Include accessories in shops")
    parser.add_argument("--more-items", action="store_true", help="Put more items in each shop")
    parser.add_argument("--fewer-items", action="store_true", help="Put fewer items in each shop")
    parser.add_argument("--price-variation", type=int, default=50, help="Set price variation percent (default: 50)")
    parser.add_argument("--integrate-shop-logic", action="store_true", help="Integrate shops into progression logic (default)")
    parser.add_argument("--no-integrate-shop-logic", action="store_true", help="Don't integrate shops into progression logic")
    parser.add_argument("--enforce-unique-items", action="store_true", help="Ensure weapons and armor appear only once (default)")
    parser.add_argument("--allow-duplicates", action="store_true", help="Allow duplicate weapons and armor")
    parser.add_argument("--enable-boss-magic", action="store_true", help="Enable magic usage in all boss fights")
    parser.add_argument("--skip-intro", action="store_true", help="Skip the intro sequence and start with necessary flags/items")

    args = parser.parse_args()

    # Configure options
    options = {
        "seed": args.seed if args.seed is not None else random.randint(0, 999999),
        "randomize_chests": not args.skip_chests,
        "randomize_shops": not args.skip_shops,
        "use_logic": not args.no_logic,
        "verbose": False,
        "max_attempts": 5000,
        "integrate_shop_logic": not args.no_integrate_shop_logic,
        "enforce_unique_items": not args.allow_duplicates,
        "randomize_items": True,
        "keep_consumables_in_shops": True,
        "keep_item_types": True,
        "scale_equipment": args.scale_equipment,
        "randomize_prices": True,
        "price_variation": args.price_variation,
        "items_per_shop": "more" if args.more_items else "fewer" if args.fewer_items else "normal",
        "include_accessories": args.include_accessories,
        "include_key_items": False,
        "special_items": [],
        "enable_boss_magic": args.enable_boss_magic,
        "skip_intro": args.skip_intro
    }

    # Print banner
    print("Terranigma Randomizer - Python Edition")
    print("======================================")
    print(f"Using seed: {options['seed']}")

    # Run randomizer
    try:
        result = run_randomizer(args.input_rom, args.output_rom, options)
        if result["success"]:
            print("\n" + result["message"])
            return 0
        else:
            print("\nError: " + result["error"])
            return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1

def run_randomizer(input_path, output_path, options):
    """Run the randomizer with the specified options"""
    try:
        # Load the ROM
        print(f"Loading ROM: {input_path}")
        rom_data = rom.read_rom(input_path)
        print(f"Successfully loaded ROM: {len(rom_data)} bytes")

        # Create a copy of the ROM data to modify
        randomized_rom = bytearray(rom_data)

        # Handle different randomization strategies
        if options["randomize_chests"] and options["randomize_shops"] and options["integrate_shop_logic"]:
            print("\nRandomizing with unique item placement and shop integration...")
            
            if options["enforce_unique_items"]:
                result = integration.randomize_with_unique_items(randomized_rom, options)
            else:
                result = integration.randomize_with_shop_integration(randomized_rom, options)
            
            if not result["success"]:
                return result
            
            randomized_rom = result["rom"]
            chest_spoiler_log = result.get("chest_spoiler_log", [])
            randomized_shops = result.get("shop_spoiler_log", [])
            key_items_in_shops = result.get("key_items_in_shops", [])
            unique_items_in_shops = result.get("unique_items_in_shops", [])
        else:
            # Original separate randomization
            chest_spoiler_log = []
            randomized_shops = []
            key_items_in_shops = []
            unique_items_in_shops = []
            
            if options["randomize_chests"]:
                print("\nRandomizing chests...")
                chest_result = chest.randomize_chests(randomized_rom, options)
                randomized_rom = chest_result["rom"]
                chest_spoiler_log = chest_result["spoiler_log"]
            
            if options["randomize_shops"]:
                print("\nRandomizing shops...")
                shop_result = shop.randomize_shops(randomized_rom, options)
                randomized_rom = shop_result["rom"]
                randomized_shops = shop_result["shops"]

        # Apply ASM patches
        if options.get("enable_boss_magic") or options.get("skip_intro"):
            print("\nApplying ASM patches...")
            randomized_rom = asm.apply_asm_patches(randomized_rom, options)

        # Write the randomized ROM
        print(f"\nWriting randomized ROM to: {output_path}")
        rom.write_rom(output_path, randomized_rom)

        # Generate spoiler log
        spoiler_path = str(Path(output_path).with_suffix('.txt'))
        print(f"Generating spoiler log: {spoiler_path}")
        
        # Generate appropriate spoiler log based on options
        if options["randomize_chests"] and options["randomize_shops"] and options["integrate_shop_logic"]:
            # Use enhanced spoiler for integrated logic
            spoiler_content = spoilers.generate_enhanced_spoiler_text({
                "chest_spoiler_log": chest_spoiler_log,
                "shop_spoiler_log": randomized_shops,
                "key_items_in_shops": key_items_in_shops,
                "unique_items_in_shops": unique_items_in_shops
            }, options['seed'])
        elif options["randomize_chests"] and not options["randomize_shops"]:
            # Chest-only spoiler
            spoiler_content = spoilers.generate_chest_spoiler_text(chest_spoiler_log)
        elif options["randomize_shops"] and not options["randomize_chests"]:
            # Shop-only spoiler
            spoiler_content = spoilers.generate_shop_spoiler_text(randomized_shops, options['seed'])
        else:
            # Combined but not integrated
            spoiler_content = ""
            if options["randomize_chests"]:
                spoiler_content += spoilers.generate_chest_spoiler_text(chest_spoiler_log)
                spoiler_content += "\n\n"
            if options["randomize_shops"]:
                spoiler_content += spoilers.generate_shop_spoiler_text(randomized_shops, options['seed'])
        
        with open(spoiler_path, 'w') as f:
            f.write(spoiler_content)

        return {
            "success": True,
            "message": f"Randomization complete!\nOutput: {output_path}\nSpoiler log: {spoiler_path}"
        }
        
    except Exception as e:
        import traceback
        return {
            "success": False,
            "error": f"{str(e)}\n{traceback.format_exc()}"
        }

if __name__ == "__main__":
    sys.exit(main())