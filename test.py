print("Hello World!")  # this line prints "Hello World!"

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
    