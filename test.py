"""print("Hello World!")  # this line prints "Hello World!"

# this line asks for user input at runtime
name = input("What is your name? ")

# this line prints
print("Hello world, welcome " + name + " !")

# commenting out the below codes will disable the codes, so that they do not run

# for i in range(1000):
#     print(f'{i+1}: {name}')

# in the codes below, we are comparing the values of two numbers denoted by a and b
a = input("Value of a: ")
b = input("Value of b: ")
if b > a:
    print("b is greater than a")
elif b == a:
    print("b is equal to a")
elif b < a:
    print("b is less than a")

name = input("what is your name?")
print("hello , welcome " + name + " !" )

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess !=random_number:
        guess = int(input(f'guess a number between 1 and {x}:'))
        if guess < random_number:
            print("sorry guess again.Too low.")
        elif guess > random_number:
            print("sorry guess again.Too high.")
    print(f'Yay,you have guess the number {random_number}')


guess(10)"""