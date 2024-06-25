# Replace ___ with your code

# get integer input from the user
n = int(input("n: "))

# use a while loop to print numbers from n to 1
i = 0
while i < n:
    print(n-i)
    i += 1
print(f'last value of i is {i}')

import random


def get_random_word():
    words = ["python", "computer", "programming", "game", "challenge", "code"]
    return random.choice(words)


def print_backwards(word):
    reversed_word = word[::-1]  # Reverse the word
    print(f"Guess the word: {reversed_word}")
    return reversed_word


def play_game():
    print("Welcome to the Print Backwards Game!")
    print("Try to guess the word that is printed backwards.")

    while True:
        word = get_random_word()
        reversed_word = print_backwards(word)

        guess = input("Your guess: ").strip().lower()

        if guess == word:
            print("Congratulations! You guessed correctly!")
        else:
            print(f"Sorry, the correct word was '{word}'.")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
