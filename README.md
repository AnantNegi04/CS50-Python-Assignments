# CS50P: Python Lectures & Problem Sets

My code from Harvard's [CS50's Introduction to Programming with Python](https://cs50.harvard.edu/python/): practice scripts written while following the lectures, plus solutions to the course problem sets.

I'm using this course to build a solid Python foundation for a career in QA engineering and test automation, so the later problem sets lean heavily on **testing with `pytest`**, input validation, and edge-case handling.

## Repository Structure

```
.
├── assignment/                          # Problem set solutions
│   ├── problem_set0/ … problem_set8/
├── Introduction to Python/              # Lecture practice: variables, input, basic logic
├── Function Loops Conditionals and Errors/
├── Libraries/                           # random, statistics, sys, APIs (requests)
├── Unit Tests/                          # Writing and testing functions (assert, pytest)
├── Regular Expression/                  # re module: validation and formatting
├── FileIO/                              # Reading/writing text and CSV files
├── OOP/                                 # Classes, objects, inheritance
├── YAML/                                # YAML / JSON / XML data formats
├── Etcetra/                             # Misc topics: unpacking, global, sleep, cowsay
└── test/                                # Test examples
```

## Problem Sets

| Set | Topic | Programs |
|-----|-------|----------|
| 0 | Functions & variables | `indoor`, `playback`, `faces`, `einstein`, `tip` |
| 1 | Conditionals | `deep`, `bank`, `extension`, `interpreter`, `meal` |
| 2 | Loops | `camel`, `coke`, `twttr`, `plates`, `nutrition` |
| 3 | Exceptions | `fuel`, `taqueria`, `outdated` |
| 4 | Libraries | `emojize`, `figlet`, `adieu`, `game`, `professor`, `bitcoin` |
| 5 | Unit tests | `twttr`, `bank`, `plates`, `fuel` (each with a `test_*.py`) |
| 6 | File I/O | `line`, `pizza`, `scourgify`, `shirt` |
| 7 | Regular expressions | `numb3rs`, `watch`, `working`, `response`, `um` |
| 8 | Object-oriented programming | `seasons`, `jar` (with tests) |

## Topics Covered

- Core Python: variables, types, conditionals, loops, functions
- Exception handling and defensive input validation
- Standard library and third-party packages
- Unit testing with `pytest`, including testing for failure cases
- Regular expressions for parsing and validating text
- File handling with CSV, JSON, YAML, and image files
- Classes, properties, and basic OOP design
- Command-line programs using `sys.argv`

## Getting Started

**Requirements:** Python 3.10+

```bash
git clone https://github.com/AnantNegi04/CS50-Python-Assignments.git
cd CS50-Python-Assignments

# Optional: create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Third-party packages used across the repo
pip install requests pytest inflect emoji cowsay pyfiglet pyttsx3 tabulate validator-collection Pillow
```

**Run a program:**

```bash
python assignment/problem_set2/camel.py
```

**Run the tests for a problem set:**

```bash
cd assignment/problem_set5
pytest
```

Some programs take command-line arguments, for example:

```bash
cd assignment/problem_set6
python shirt.py before1.jpg after1.jpg
```

## Notes

- `bitcoin.py` (problem set 4) calls a third-party price API and needs your own API key to run.
- Solutions are my own work and are shared for learning and reference. If you're taking CS50P yourself, try the problems first. CS50's [academic honesty policy](https://cs50.harvard.edu/python/honesty/) applies.

## Author

**Anant Negi** — [GitHub](https://github.com/AnantNegi04) · [LinkedIn](https://www.linkedin.com/in/anant-negi-5a0811401)
