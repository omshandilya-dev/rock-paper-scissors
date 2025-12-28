# CLI rock-paper-scissors

​A simple, interactive Rock Paper Scissors game played against the computer. Built to demonstrate basic Python loops, conditional logic, and the random module.

## How it works
The game uses a simple dictionary to map out the "who beats who" logic. It keeps running in a loop, keeping track of your wins versus the computer's wins, until you type 'q' to exit.

## How to play
1. Make sure you have Python installed.
2. Download `rock_paper_scissors.py`.
3. Run it in your terminal: `python rock_paper_scissors.py`
4. Pick Rock, Paper, or Scissors (or 'Q' to see your final score and quit).

## Logic
I used a dictionary called `beats` to handle the win conditions. If your input matches the key that points to the computer's choice, you win. It's cleaner than writing a dozen `if/elif` statements.
