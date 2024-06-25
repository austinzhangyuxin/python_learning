import random


class DataTypeGuessingGame:
    def __init__(self):
        self.score = 0
        self.rounds = 5  # Number of rounds in the game

    def get_random_data(self):
        data_types = [
            ("string", "Hello, world!"),
            ("integer", 42),
            ("float", 3.14),
            ("boolean", True),
            ("list", [1, 2, 3]),
            ("dictionary", {"name": "Alice", "age": 30}),
            ("tuple", (1, 2, 3)),
            ("set", {1, 2, 3}),
            ("none", None),
        ]
        return random.choice(data_types)

    def play_round(self):
        data_type, value = self.get_random_data()
        print(f"Guess the data type of the value: {value}")
        print("Options: string, integer, float, boolean, list, dictionary, tuple, set, none")
        guess = input("Your guess: ").strip().lower()

        if guess == data_type:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {data_type}.")
        print()

    def play_game(self):
        print("Welcome to the Data Types Guessing Game!")
        print(f"You will have {self.rounds} rounds to guess the correct data types.\n")
        for _ in range(self.rounds):
            self.play_round()
        print(f"Game over! Your final score is: {self.score} out of {self.rounds}")


if __name__ == "__main__":
    game = DataTypeGuessingGame()
    game.play_game()
