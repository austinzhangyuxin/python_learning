# # get temperature in degree celsius from the user
# convert it to its equivalent floating-point number

celsius = float(input("Enter temperature in degree celsius: "))

# conversion formula
fahrenheit = (celsius * 1.8) + 32

# compute distance in miles

print(f"Temperature in Fahrenheit: {fahrenheit}")


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def convert_celsius_to_fahrenheit():
    print("Welcome to the Celsius to Fahrenheit Converter!")
    while True:
        try:
            celsius = float(input("Enter temperature in Celsius (enter 'q' to quit): "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.\n")
        except ValueError:
            choice = input("Invalid input. Do you want to quit? (yes/no): ").lower()
            if choice == 'yes' or choice == 'y' or choice == 'q':
                break
            else:
                continue


if __name__ == "__main__":
    convert_celsius_to_fahrenheit()
