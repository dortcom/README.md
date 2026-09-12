# Week 3 Assignment: Hands-On Lab — Name Splitter, Bug Hunt & First Decisions

## File Overview
* `name_greeter.py`: Takes a user's name, splits it into parts using `.split()`, and prints a personalized greeting if a full name is provided.
* `bug_hunt.py`: Contains a corrected script with `# BUG:` comments identifying and fixing syntax, variable naming, and type conversion errors.
* `ticket_checker.py`: Prompts for age, evaluates an `is_adult` Boolean condition (`age >= 18`), prints the Boolean value, and displays the corresponding ticket price using `if / else`.

## Reflection
The bug that took the longest to resolve was the `TypeError` in `bug_hunt.py` when attempting to calculate `age + 1`. The Python error message `TypeError: can only concatenate str (not "int") to str` helped pinpoint the issue by clarifying that input values are treated as strings by default and must be converted using `int()` before performing arithmetic operations.
