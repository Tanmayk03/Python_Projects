# QuizGame

Simple, terminal-based quiz game written in Python.

## Features
- Multiple-choice and true/false questions
- Score tracking per session
- Timed questions (optional)
- Load questions from JSON or CSV
- Easy to extend with new question sets

## Requirements
- Python 3.8+

## Installation
1. Clone the repository:
    ```
    git clone <repo-url>
    cd QuizGame
    ```
2. (Optional) Create and activate a virtual environment:
    ```
    python -m venv .venv
    source .venv/bin/activate  # macOS / Linux
    .venv\Scripts\activate     # Windows
    ```
3. Install dependencies (if any):
    ```
    pip install -r requirements.txt
    ```

## Usage
Run the main script from the project root:
```
python main.py
```
Or, if the package exposes a module:
```
python -m quizgame
```

Follow on-screen prompts to select a quiz and answer questions. Scores are shown at the end of each session.

## Questions file format (JSON example)
Place question sets in `data/` or a specified path. Example JSON structure:
```json
[
  {
     "question": "What is the capital of France?",
     "choices": ["Paris", "London", "Berlin", "Rome"],
     "answer": 0,
     "type": "multiple_choice",
     "time_limit": 30
  },
  {
     "question": "The Earth is flat.",
     "answer": false,
     "type": "boolean"
  }
]
```
- `answer` for multiple choice is the zero-based index of the correct choice.
- `time_limit` (optional) is in seconds.

## Configuration
- Configure default question folder, time limits, and UI settings in `config.yaml` (create if missing) or via environment variables as supported.

## Testing
Run unit tests (if present):
```
pytest
```

## Contributing
- Fork the repository
- Create a feature branch
- Open a pull request with a clear description and tests

## Contact
Issues and feature requests: create an issue in the repository.
