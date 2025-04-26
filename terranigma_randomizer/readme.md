# Terranigma Randomizer

A randomizer for the SNES game Terranigma that shuffles chest contents and shop items with logic to ensure the game remains completable.

## Features

- Chest content randomization with logic
- Shop item and price randomization
- Integrated progression logic to ensure the game can be completed
- Option to ensure unique weapons and armor throughout the game
- Spoiler log generation
- Command-line interface

## Installation

### From PyPI (Not yet available)

```bash
pip install terranigma-randomizer
```

### From Source

```bash
git clone https://github.com/yourusername/terranigma-randomizer.git
cd terranigma-randomizer
pip install -e .
```

## Usage

### Basic Usage

```bash
terranigma-randomizer input.sfc output.sfc
```

### With Options

```bash
terranigma-randomizer input.sfc output.sfc --seed 12345 --scale-equipment --include-accessories
```

### Available Options

- `--seed NUMBER`: Specify a random seed for reproducible randomization
- `--skip-chests`: Skip chest randomization
- `--skip-shops`: Skip shop randomization
- `--no-logic`: Use purely random chest placement (not recommended)
- `--scale-equipment`: Scale shop equipment to game progression
- `--include-accessories`: Include accessories in shops
- `--more-items`: Put more items in each shop
- `--fewer-items`: Put fewer items in each shop
- `--price-variation NUMBER`: Set price variation percent (default: 50)
- `--integrate-shop-logic`: Integrate shops into progression logic (default: true)
- `--no-integrate-shop-logic`: Don't integrate shops into progression logic
- `--enforce-unique-items`: Ensure weapons and armor appear only once (default: true)
- `--allow-duplicates`: Allow duplicate weapons and armor

## How It Works

The randomizer uses a logical placement system to ensure that key items are placed in a way that makes the game completable. It analyzes the game's progression structure and places items accordingly.

Key features of the logic system:
- Places essential progression items in accessible locations
- Ensures that items required to reach certain areas are available before those areas
- Balances item placement between chests and shops
- Can enforce unique equipment throughout the game

## Spoiler Logs

Spoiler logs are generated with each randomization, containing information about item placement, key locations, and a suggested progression path.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Credits

- Original game developed and owned by Quintet Co., Ltd. and published by Enix
- All randomization code developed by the Terranigma Randomizer Team
