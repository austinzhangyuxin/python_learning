# print("Hello World!")  # this line prints "Hello World!"
#
# # this line asks for user input at runtime
# name = input("What is your name? ")
#
# # this line prints
# print("Hello world, welcome " + name + " !")
#
# # commenting out the below codes will disable the codes, so that they do not run
#
# # for i in range(1000):
# #     print(f'{i+1}: {name}')
#
# # in the codes below, we are comparing the values of two numbers denoted by a and b
# a = input("Value of a: ")
# b = input("Value of b: ")
# if b > a:
#     print("b is greater than a")
# elif b == a:
#     print("b is equal to a")
# elif b < a:
#     print("b is less than a")
#
# name = input("what is your name?")
# print("hello , welcome " + name + " !" )
#
# import random
#
# def guess(x):
#     random_number = random.randint(1, x)
#     guess = 0
#     while guess !=random_number:
#         guess = int(input(f'guess a number between 1 and {x}:'))
#         if guess < random_number:
#             print("sorry guess again.Too low.")
#         elif guess > random_number:
#             print("sorry guess again.Too high.")
#     print(f'Yay,you have guess the number {random_number}')
#
#
# guess(10)

# Replace ___ with your code
#
# # get the integer inputs for n1 and n2
# n1 = int(input("n1: "))
# n2 = int(input("n2:"))
#
# # create a temporary variable and swap the values
# temp = n2
# n2 = n1
# n1 = temp
#
# # print the values of n1 and n2
# print(n1)
# print(n2)

# Replace ___ with your code

# Replace ___ with your code

# get integer input from the user
#number = int(input())

# check if the number is not divisible by 3
# and print the result
# print(number % 3 != 0)

# Replace ___ with your code

# get integer input from the user
# number = int(input())
#
# check if number is positive, negative or 0
# if number > 0:
#     print("positive")
# elif number < 0:
#     print("negative")
# else:
#     print("zero")
#
# # Replace ___ with your code
#
# # get integer input from the user
# number = int(input("number: "))
#
# # check odd/even
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")

number = 1

while number <= 10:
    print(f"Number: {number}")
    number += 2

# # Replace ___ with your code

# # get integer input from the user
# n = int(input("n: "))

# # use a while loop to print numbers from n to 1
# number = 1
# while number <= n:
#     print(f"Number: {number}")

# get integer input from the user
n = int(input())

i = n
while i >= 1:
    print(i)
    i = i - 1