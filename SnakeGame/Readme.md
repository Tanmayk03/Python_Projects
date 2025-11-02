# Snake Game

A classic Snake game implemented in Python.

## Description

This is a simple Snake game where the player controls a snake that grows longer as it eats food. The game ends if the snake hits the walls or itself.

## Features

- Simple and intuitive controls
- Score tracking
- Increasing difficulty as the snake grows
- Classic retro-style gameplay

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone this repository
```bash
git clone https://github.com/yourusername/SnakeGame.git
```

2. Install required packages
```bash
pip install pygame
```

A quick guide to playing Snake and getting the most out of the game.

1. Run the game
```bash
python main.py
```

2. Objective
- Eat the food to grow and increase your score.
- The game ends if the snake collides with the walls or with itself.

3. Controls
- Move: Arrow keys or W/A/S/D
- Pause / Resume: P
- Restart (after game over): R or press Enter (if supported)
- Quit: Esc or close the game window

4. Scoring & difficulty
- Each food item increases your score (typically +1 per food).
- Speed increases gradually as the snake grows to raise the challenge.

5. Tips & strategy
- Avoid sharp turns when the snake is long; plan several moves ahead.
- Use open space to turn safely; don’t get boxed in by your tail.
- When close to walls, slow down directional changes and seek central space.

6. Customization & troubleshooting
- Adjust game speed, grid size, and colors in the source (look for speed/grid constants or a config section).
- If the game window won't open, ensure Pygame is installed (`pip install pygame`) and you are using a compatible Python version.

7. Reporting issues
- If you encounter bugs or want feature requests, open an issue in the repository with reproduction steps and your environment (OS, Python, Pygame versions).
