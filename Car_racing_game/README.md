# Car Racing Game

A car racing game built with Python and Pygame. Avoid enemy cars, collect power-ups, and achieve the highest score.

## Installation

1. Install Pygame:
   ```bash
   pip install pygame
   ```

2. Run the game:
   ```bash
   python car_racing_game.py
   ```

## Controls

- **Move**: Arrow keys or WASD
- **Quit**: ESC

**Note**: Car can only turn when moving. Reverse steering is automatically adjusted.

## Gameplay

- Avoid enemy cars (they deal damage)
- Collect power-ups for speed boosts and health
- Score points by surviving and collecting items
- Game gets harder as you advance levels

## Scoring

- Survival: +1 point per frame
- Enemy car passed: +10 points
- Power-up collected: +50 points
- New level every 1000 points

## Power-ups

- **Yellow**: Speed boost (permanent)
- **Green**: Health pack (+30 health, capped at 100)
- **Blue**: Shield (+10 health, capped at 100)

## Level Scaling

- Enemy spawn frequency increases by 20% per level
- Max enemy cars increases by 1 per level (capped at 8)
- Enemy speed increases by 0.5 per level
- Spawn timing gets faster each level

## Technical Details

- **Resolution**: 800x600 pixels
- **FPS**: 60 FPS
- **Car Size**: 60x60 pixels
- **Road Boundaries**: Automatic enforcement

## File Structure

```
Car Racing Game/
├── car_racing_game.py
├── requirements.txt
├── README.md
└── assets/
    ├── topcar.png      # Player car
    ├── redcar2.png     # Red enemy
    ├── bluecar.png     # Blue enemy
    └── yellowcar.png   # Yellow enemy
```

## Troubleshooting

- **Game won't start**: Install pygame with `pip install pygame`
- **Poor performance**: Close other applications
- **Controls not working**: Make sure game window is focused