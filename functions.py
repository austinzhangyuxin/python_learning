def happy_birthday(name, age):
    print(f"happy_birthday to {name} at {age} years old!")


def multiply(x, y):
    result = x * y
    print(f'The result of {x} multiply by {y} is {result}.')
    # return x * y


multiply(4, 5)

multiply(10,40)

multiply(100, 80)


def exponential(base, power):
    result = base ** power
    print(f'The result of {base} to the power of {power} is {result}.')
    # return x * y

exponential(4, 2)

exponential(10, 100)

# define print_numbers() function
def print_numbers():
    print(5)
    print(100)


# call print_number() twice
print_numbers()
print_numbers()


# define a function to add numbers
def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is", result)

# Replace ___ with your code

# create the get_product() function
def get_product(number1, number2):
    result = number1 * number2
    return result

# get integer inputs from the user
n1 = int(input(""))
n2 = int(input(""))

# call the function with n1 and n2 as arguments
# and print the return value

total = get_product(n1, n2)
print(total)


number1 = 5
number2 = 6
add_numbers(number1, number2)


# Replace ___ with your code

# define the function add_three_numbers()
def add_three_numbers(n1, n2, n3):
    result = n1 + n2 + n3
    print(result)

# take input for num1, num2, num3
num1 = int(input(""))
num2 = int(input(""))
num3 = int(input(""))

# call the function with num1, num2 and num3
add_three_numbers(num1, num2, num3)

def add_numbers(n1, n2):
    result = n1 + n2
    return result

total = add_numbers(10, 20)
print(total)     # 30

print(add_numbers(20, 30))    # 50

# Replace ___ with your code

# define the is_positive_or_negative() function
def is_positive_or_negative(number):
    if number >= 0:
        return True
    else:
        return False

# take integer input from the user
input_number = int(input("num: "))

# call the function
print(is_positive_or_negative(input_number))