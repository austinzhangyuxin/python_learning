# Program to convert distance in kilometer to miles
# The distance will be entered by the user

# get distance in kilometers and
# convert it to its equivalent floating-point number

# two steps involved in the following:
# 1) input("Enter distance in km: ") gives user input in km --> string (always a string from user input)
km = input("Enter distance in km: ")
print(type(km))
# 2) convert user input from string to float
km = float(km)
print(type(km))

# km = float(input("Enter distance in km: "))


# conversion ratio
# 1 kilometer = 0.621 miles
km_miles_ratio = 0.621

# compute distance in miles
miles = km * km_miles_ratio
print(f"Distance in miles: {miles}")

# km = input("Enter distance in km: ")
# print(f"Data type of km is {type(km)}")