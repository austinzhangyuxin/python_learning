import random

# List of words for the game
words = [
    'python', 'hangman', 'program', 'computer', 'language',
    'algorithm', 'developer', 'software', 'engineering', 'keyboard'
]


def choose_word(words):
    """Choose a random word from the list."""
    return random.choice(words)


def display_word(word, guessed_letters):
    """Display the word with correctly guessed letters and blanks for unguessed letters."""
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word.strip()


def hangman():
    """Main hangman game function."""
    word = choose_word(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word.")

    while True:
        print("\nAttempts left:", attempts)
        displayed = display_word(word, guessed_letters)
        print(displayed)

        if '_' not in displayed:
            print("\nCongratulations! You guessed the word:", word)
            break

        if attempts == 0:
            print("\nGame Over! The word was:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess!")
        else:
            print("Correct guess!")


if __name__ == "__main__":
    hangman()
