import random

def play_game():
    computer_win = 0
    user_win = 0

    # Win mapping: Key win over Value
    beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    while True:
        user_input = input("\nPick Rock/Paper/Scissors or Q to quit: ").lower()

        if user_input == "q":
            print(f"\nFinal Scores:\nComputer: {computer_win}\nYou: {user_win}\nGAME OVER")
            break

        if user_input not in beats:
            print("Invalid choice. Please pick Rock, Paper, or Scissors.")
            continue

        computer_pick = random.choice(list(beats.keys()))
        print(f"Computer picked: {computer_pick}")

        if user_input == computer_pick:
            print("It's a draw!")
        elif beats[user_input] == computer_pick:
            print("You win!")
            user_win += 1
        else:
            print("Computer wins!")
            computer_win += 1

if __name__ == "__main__":
    play_game()
