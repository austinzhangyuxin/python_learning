number = int(input("enter a number: "))

# iterate a loop from 1 to 5
for i in range(1, 6):
    # compute product in each iteration of the loop
    # product will 9 * 1 in first iteration,
    # 9 * 2 in second iteration and so on
    product = number * i
    print(product)
# -------------------------------------------
number = int(input("enter a number: "))

# iterate a loop from 1 to 5
for i in range(1, 6):
    # compute product in each iteration of the loop
    product = number * i
    print(f"{number} * {i} = {product}")
# -------------------------------------------
# get integer input from the user
n = int(input("enter a number: "))

# create multiplication table from 6 to 9
for i in range(6, 10):
    product = n * i
    print(f"{n} times {i} is {product}")
