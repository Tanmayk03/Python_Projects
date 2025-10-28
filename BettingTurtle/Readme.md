# BettingTurtle

Lightweight Python project for simulating and testing betting strategies using a "turtle"-style simulation harness. Useful for exploring stake sizing, bankroll management, and strategy backtesting with simple visual/debug output.

## Features
- Simple simulation loop for sequential bets
- Configurable strategies and stake-sizing rules
- Bankroll tracking and basic metrics (ROI, drawdown)
- CLI runner for quick experiments
- Extensible for custom strategies and data sources

## Requirements
- Python 3.8+
- (Optional) virtualenv or venv for isolation

## Installation
1. Clone or copy this repository to your machine.
2. Create and activate a virtual environment:
    ```
    python -m venv .venv
    source .venv/bin/activate   # macOS/Linux
    .venv\Scripts\activate      # Windows (PowerShell)
    ```
3. Install dependencies (if a requirements.txt exists):
    ```
    pip install -r requirements.txt
    ```

## Project layout (suggested)
- betting_turtle/
  - __init__.py
  - core.py         # simulation engine, bankroll, runner
  - strategies.py   # built-in strategies
  - config.py       # default config and loaders
  - cli.py          # command-line entrypoint
- tests/
- README.md
- requirements.txt

## Usage
Run the main CLI or script to start a simulation:
```
python -m betting_turtle.cli --config config.yml
```
Or run a simple script:
```py
from betting_turtle import core, strategies

sim = core.Simulation(bankroll=1000, strategy=strategies.TurtleStrategy())
sim.run(n_rounds=1000)
print(sim.summary())
```

## Configuration example (config.yml)
```yaml
bankroll: 1000
rounds: 500
strategy:
  name: turtle
  params:
     base_unit: 1
     max_unit: 10
risk:
  max_drawdown_pct: 30
logging: info
```

## Extending
- Add new strategy classes in strategies.py (implement decide_bet and update_state)
- Hook custom data sources for real market/odds data
- Add more metrics and visualizations (matplotlib, pandas)

## Testing
Run unit tests:
```
pytest
```

## Contributing
- Fork, create a feature branch, and open a PR
- Keep changes focused and include tests for logic
- Follow project code style (PEP8)

