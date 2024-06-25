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
