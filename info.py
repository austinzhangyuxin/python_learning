def display_info(name, location):
    """
    Function to display name and location.
    Prints the name and location in two separate lines.
    """
    print(name)
    print(location)


def main():
    # Get string input from the user and assign it to the country variable
    country = input("Enter your country: ")

    # Call the display_info function with "Magnus" and the country variable
    display_info("Magnus", country)


if __name__ == "__main__":
    main()


def find_sum(n):
    """
    Function to compute the sum of the first n natural numbers.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def main():
    # Get an integer input for the number variable
    number = int(input("Enter a positive integer: "))

    # Call the find_sum function and pass number as an argument
    sum_of_natural_numbers = find_sum(number)

    # Print the return value
    print(f"The sum of the first {number} natural numbers is: {sum_of_natural_numbers}")


if __name__ == "__main__":
    main()
