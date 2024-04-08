age1 = 21
age2 = 18

# 21 less than 21 is False
print(age1 < 21)

# 21 less than or equal to 21 is True
print(age1 <= 21)

# 18 less than 21 is True
print(age2 < age1)

# 18 less than or equal to 18 is True
print(age2 <= age2)

# 18 less than 17 is False
print(age2 < 17)

# 18 less than or equal to 18 is True
print(age2 <= 18)

# Replace ___ with your code

# get two integer inputs from the user
var1 = int(input("var1"))
var2 = int(input("var2"))
# compare var1 and var2 using comparison operators and print the results
print(f"var1 < var2: {var1 < var2}")
print(f"var1 > var2: {var1 > var2}")
print(f"var1 != var2: {var1 != var2}")

# Replace ___ with your code

# get string inputs from the user
var1 = input("var1: ")
var2 = input("var2: ")

# check if two strings are equal and print the result
print(f"{var1 == var2}")