import random


def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple", "watermelon", "strawberry", "blueberry"]
    return random.choice(words)


def play_game():
    word_to_guess = choose_word()
    word_length = len(word_to_guess)
    guessed_letters = set()
    attempts = 0
    max_attempts = 6

    print("Welcome to Guess the Word Game!")
    print(f"The word to guess has {word_length} letters.")

    while True:
        print("\n")
        print(" ".join(letter if letter in guessed_letters else "_" for letter in word_to_guess))

        if set(word_to_guess) == guessed_letters:
            print("Congratulations! You guessed the word correctly.")
            break

        if attempts >= max_attempts:
            print(f"Game over! You ran out of attempts. The word was '{word_to_guess}'.")
            break

        guess = input("Guess a letter or the whole word: ").lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try another letter.")
            elif guess in word_to_guess:
                guessed_letters.add(guess)
                print(f"Good guess! '{guess}' is in the word.")
            else:
                attempts += 1
                print(f"Sorry, '{guess}' is not in the word. Attempts left: {max_attempts - attempts}")
        elif len(guess) == word_length:
            if guess == word_to_guess:
                print(f"Congratulations! You guessed the word correctly.")
                break
            else:
                attempts += 1
                print(f"Sorry, '{guess}' is not the word. Attempts left: {max_attempts - attempts}")
        else:
            print("Invalid input. Please enter a single letter or the whole word.")


if __name__ == "__main__":
    play_game()

