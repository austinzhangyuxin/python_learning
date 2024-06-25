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

def km_to_miles(km):
    miles = km * 0.621371
    return miles


def convert_km_to_miles():
    print("Welcome to the Kilometers to Miles Converter!")
    while True:
        try:
            km = float(input("Enter distance in kilometers (enter 'q' to quit): "))
            if km < 0:
                print("Distance cannot be negative. Please enter a positive number.")
                continue
            miles = km_to_miles(km)
            print(f"{km} kilometers is equal to {miles:.2f} miles.\n")
        except ValueError:
            choice = input("Invalid input. Do you want to quit? (yes/no): ").lower()
            if choice == 'yes' or choice == 'y' or choice == 'q':
                break
            else:
                continue


if __name__ == "__main__":
    convert_km_to_miles()
