age = 20
print("Age:", age)
print("hello\nworld")
colour1 = "pink"
colour2 = "blue"
colour1 = colour2
print(colour2)

# Replace ___ with your code

# create the pen_number and student_number variables
pen_number = 14
student_number = 3
# compute the number of pens each student will get and print it
# hint: find the quotient
print(pen_number//student_number)

# compute and print the number of remaining pens
# hint: find the remainder
print(pen_number%student_number)

base = 4
power = 3

result = base ** power
print(result)

base = 2.5
power = 3

result = base ** power
print(result)

# Replace ___ with your code

# create the length variable
length = 5

# calculate the volume
volume = length ** 3

# print the volume
print(volume)


# Replace __ with your code

# create the fee and discount_percent variables
fee = 1536
discount_percent = 10
# compute discount and assign it to the discount variable
discount = (discount_percent / 100) * fee
# print(f'Discount is: {discount}')

# compute and print the fee you have to pay
fee_payable = fee - discount
# print(f'Fee to pay: {fee_payable}')
print(fee_payable)

# Operator	Syntax	Meaning
# +	x + y	Addition
# -	x - y	Subtraction
# *	x * y	Multiplication
# /	x / y	Division
# //	x // y	Quotient
# %	x % y	Remainder
# **	x ** y	Exponentiation

# get the data type of 5
data_type = type(5)

print("Data type:", data_type)

# get the data type of 65.50
data_type = type(65.50)

print("Data type:", data_type)

float_number = 15.0

# convert float to integer
integer_number = int(float_number)

print(integer_number)  # Output: 15

string_number = "15"

# convert string to integer
# integer_number will contain 15
integer_number = int(string_number)

print(integer_number)  # Output: 15

# variables
name = "Alice"
location = "Wonderland"

# insert the values of the variables inside an f-string
print(f"My name is {name} and I live in {location}")

# Write code here
# name = input("what is your name:")
# location = input("were do you live:")
# print(f"My name is {name} and i live in {location}")

# input from user is always a string
x = int(input("x: "))
y = int(input("y: "))

# convert string input to integers
# x = int(x)
# y = int(y)

print(f"result = {x - y}")