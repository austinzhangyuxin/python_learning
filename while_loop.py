# Replace ___ with your code

# take an integer input from the user
n = int(input("n: "))

# create a variable total and assign 1
total = 1

# create a variable i and assign 1
i = 1

# write your code here
while i <= n:
    total = total * i
    i = i + 1

print(total)

age = int(input("enter your age"))

while age < 0:
    print("age can't be negative.")
    age = int(input("enter your age"))
else:
    print(f"your age is {age} years old.")

food = input("enter a food you like(q to quit)")
while not food == "q":
    print(f"you like {food}")
    food = input("enter another food you like(q to quit)")

print("bye")


# get float input from the user
n = float(input())

# create a variable total and assign 0
total = 0

# loop as long as n is not negative and not 0
while n > 0:
    total += n
    n = float(input())

# print the total
print(total)

while True:
    n = int(input())

    if n < 1 or n > 100:
        break

    print(n)

topic = input('What are you learning? ')

while topic != "Python":
    print('You are not learning', topic)
    topic = input('What are you learning? ')

print('You are indeed learning', topic)

# Output:
# What are you learning? Java
# You are not learning Java
# What are you learning? Python
# You are indeed learning Python