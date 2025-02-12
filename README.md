# Lexical Decision Task 🎯📚💡

**Final Project for Intermediate Programming and Problem Solving** \
Author: Zoe Burke (123718179)\
University College Cork - School of Computer Science 

## Table of Contents 

- [Project Overview](#project-overview)
- [File Structure](#file-structure)
- [How to Run](#how-to-run)
- [Code Explanation](#code-explanation)
- [Extra Features](#extra-features)

## Project Overview 

This project implements a **Lexical Decision Task (LDT)**, where users identify whether a set of words are English or not. The program utilizes object-oriented principles, with classes designed for file handling and participant management. 🚀

## File Structure 

```
├── main.py               # Entry point of the application
├── filereader.py         # Contains FileReader and WordFileReader classes
├── participant.py        # Contains TrialParticipant class
└── words.txt             # Input file containing words
```

## How to Run 

1. Ensure `main.py`, `filereader.py`, `participant.py`, and `words.txt` are in the same directory.
2. Run the script:
   ```bash
   python main.py
   ```
3. Follow the on-screen instructions to participate in the task. 

## Code Explanation 

### `main.py` 

- **Imports:** `WordFileReader` from `filereader.py` and `TrialParticipant` from `participant.py`.
- **Entry Point:**
  ```python
  if __name__ == "__main__":
  ```
  Ensures the script runs only when executed directly. 
- **Game Flow:**
  1. Load words from `words.txt`.
  2. Create a `TrialParticipant` instance.
  3. Print game introduction and request user consent.
  4. Run the game loop until no words remain.
  5. Display results. 

### `filereader.py` 

- **Classes:**
  - `FileReader`: Handles basic file operations (read, count lines).
  - `WordFileReader`: Inherits from `FileReader` and processes words into a nested dictionary.
- **Key Methods:**
  - `all_rounds()`: Converts file content into a dictionary of rounds.
  - `get_rounds_at()`, `get_round_range()`, `random_rounds()`, `exclude_round_range()`: Provide flexible word selection. 

### `participant.py` 

- **Class:** `TrialParticipant`
- **Responsibilities:**
  - Manage participant data (name, position, score).
  - Handle responses and validate answers.
  - Allow dynamic updates to the word set. 

## Extra Features 🚀

- **Dynamic Word Changes:** After three rounds, users can load a new word file.
- **Enhanced Feedback:** Personalized feedback when participants achieve more than four correct answers.
- **Input Validation:** Robust checks to ensure data integrity when updating word sets. 

## Example Interaction 🖥️💬🎯

````bash
Welcome to the Lexical Decision Task, John Doe!
In this task, you will be presented with four words.
Your task is to select whether all four words are in English.

Do you consent to engaging with the experiment? (1 for yes, 2 for no): 1

The words are: apple, banana, orange, pear
Are all these words in English? (y/n): y
That's correct!
...
Experiment ended. Here are your results, John:
Correct = 5 | Incorrect = 1
``` 

````
