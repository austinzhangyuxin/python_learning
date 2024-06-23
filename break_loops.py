# Replace ___ with your code

# get an integer input from the user
n = int(input("enter a number: "))

# using a loop, iterate from 1 to n (inclusive) and print n
for i in range (1, n+1):
    print(i)

    # if the value of i is 3, break the loop
    if i == 3:
        break


# initial value of total will be 0
total = 0

n = float(input("Enter a number: "))

# loop until n is not equal to 0
while n != 0:
    # add the value of n to total
    total = total + n

    # take the input again
    n = float(input("Enter a number: "))

# print the total
print(f"Result: {total}")

# initial value of total will be 0
total = 0

# the condition of the loop is always True
# the only way to end this loop is by using break
while True:

    n = float(input("Enter a number: "))

    # if user enters 0, end the loop
    if n == 0:
        break

    # add the value of n to total
    total = total + n

# print the total
print(f"Result: {total}")

total = 0

while True:
    # get integer input
    n = int(input("enter a number"))

    if n <= 0:
        break

    total = total + n

# print the total
print(total)

for i in range(1, 101):

    if i == 3:
        break

    print(i)