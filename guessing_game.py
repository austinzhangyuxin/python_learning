import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a random number between 1 and {x}: '))
        if guess < random_number:
            print("sorry guess again.Too low.")
        elif guess > random_number:
            print("sorry guess again.Too high.")
    print(f"Yay, congrats you have guessed the number {random_number} correctly! ")


guess(10)


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            trial = random.randint(low, high)
        else:
            trial = low
        feedback = input(f"Is {trial} too high (H), too low (L), or correct (C)??").lower()
        if feedback == 'h':
            high = trial - 1
        elif feedback == 'l':
            low = trial + 1

    print(f'Yay, the computer guessed your number, {trial}, correctly!')


computer_guess(1000)
