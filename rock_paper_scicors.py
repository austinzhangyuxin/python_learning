import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock, paper, scissors): ")

    print(f"player:{player}")
    print(f"computer:{computer}")

    if player == computer:
        print("it's a tie!")
    elif player == "rock" and computer == "scissors":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win")
    elif player == "scissors" and computer == "paper":
        print("you win")
    else:
        print("you lose")

    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        running = False

print("thanks for playing!")

import random


def get_user_choice():
    while True:
        print("\nChoose your move:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit game")

        try:
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_computer_choice():
    return random.randint(1, 3)


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 1 and computer_choice == 3) or \
            (player_choice == 2 and computer_choice == 1) or \
            (player_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    player_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()

        if user_choice == 4:
            print("\nExiting game...")
            break

        computer_choice = get_computer_choice()

        print(f"\nYou chose: {get_choice_name(user_choice)}")
        print(f"Computer chose: {get_choice_name(computer_choice)}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score - You: {player_score}  Computer: {computer_score}")


def get_choice_name(choice):
    if choice == 1:
        return "Rock"
    elif choice == 2:
        return "Paper"
    elif choice == 3:
        return "Scissors"


if __name__ == "__main__":
    print("Welcome to the Advanced Rock, Paper, Scissors Game!")
    play_game()

import tkinter as tk
import random


class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")

        # Choices
        self.choices = ["Rock", "Paper", "Scissors"]

        # Label to display result
        self.result_label = tk.Label(root, text="", font=('Arial', 18))
        self.result_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Buttons for player choices
        buttons = [
            ('Rock', 1, 0), ('Paper', 1, 1), ('Scissors', 1, 2)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: self.play(t))
            button.grid(row=row+1, column=column, padx=10, pady=10)

    def play(self, player_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(player_choice, computer_choice)
        self.result_label.config(text=f"Your choice: {player_choice}\nComputer's choice: {computer_choice}\nResult: {result}")

    def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            return "You win!"
        else:
            return "Computer wins!"


def main():
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()


if __name__ == "__main__":
    main()



import tkinter as tk
import random


class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")
        self.user_score = 0
        self.computer_score = 0
        self.rounds = 5
        self.current_round = 0

        self.choices = ["Rock", "Paper", "Scissors"]

        self.create_widgets()
        self.update_scores()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Choose Rock, Paper, or Scissors", font=("Arial", 16))
        self.label.pack(pady=10)

        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.pack(pady=10)

        self.rock_button = tk.Button(self.buttons_frame, text="Rock", command=lambda: self.play("Rock"))
        self.rock_button.grid(row=0, column=0, padx=5)

        self.paper_button = tk.Button(self.buttons_frame, text="Paper", command=lambda: self.play("Paper"))
        self.paper_button.grid(row=0, column=1, padx=5)

        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", command=lambda: self.play("Scissors"))
        self.scissors_button.grid(row=0, column=2, padx=5)

        self.result_label = tk.Label(self.master, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.master, text="", font=("Arial", 14))
        self.score_label.pack(pady=10)

    def play(self, user_choice):
        if self.current_round >= self.rounds:
            self.result_label.config(text="Game over! Reset to play again.")
            return

        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)
        self.current_round += 1

        if result == "User":
            self.user_score += 1
            self.result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}. You win this round!")
        elif result == "Computer":
            self.computer_score += 1
            self.result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}. Computer wins this round!")
        else:
            self.result_label.config(text=f"You chose {user_choice}, Computer chose {computer_choice}. It's a draw!")

        self.update_scores()

        if self.current_round >= self.rounds:
            self.announce_winner()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Draw"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            return "User"
        else:
            return "Computer"

    def update_scores(self):
        self.score_label.config(text=f"User Score: {self.user_score} | Computer Score: {self.computer_score} | Round: {self.current_round}/{self.rounds}")

    def announce_winner(self):
        if self.user_score > self.computer_score:
            winner = "You are the overall winner!"
        elif self.computer_score > self.user_score:
            winner = "Computer is the overall winner!"
        else:
            winner = "It's a draw overall!"

        self.result_label.config(text=winner)


def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
