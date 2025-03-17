# Wordle

## Overview
In this game, you should guess a five-letter word within six attempts. In each attempt, the letters will be shown in different colors. For the letters in your guess, you will be informed whether the correct letter is in the right position and if any letters are in the word but in the wrong position.

## How to Run
- Clone the repository and `cd` to it.
- Install the requirements by running this code:
```bash
pip install -r requirements.txt
```
- Add the current directory to the `PYTHONPATH` by running this code:
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
```
- run this code to start the game:
```bash
python src/run.py
```