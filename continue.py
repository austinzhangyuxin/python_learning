for number in range(1, 11):

    # condition to check odd number
    if number % 2 != 0:
        continue

    print(number)

text = input("word: ").upper()
for char in text:
    if char in "aeiou".upper():
        continue
    print(char)

# get integer input
n = int(input("enter a number"))

# use for loop to iterate from 1 to n+1 (exclusive)
for number in range(1, n + 1):
    # if number is even, skip printing of number
    if number % 2 == 0:
        continue

    # print number
    print(number)

# Replace ___ with your code

numbers = int(input("Enter a number"))

# use a for loop to print the first even number greater than 10 in the numbers list
for numbers in range(3, 24):
    if numbers > 10 and numbers % 2 == 0:
        print(numbers)
        break

for i in range(1, 6):

    if i == 3 or i == 4:
        continue

    print(i)