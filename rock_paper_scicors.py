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