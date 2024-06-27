def main():
    # Get input from the user
    n = int(input("Enter an integer (n): "))

    # Initialize the first two terms of the Fibonacci sequence
    t1, t2 = 1, 1

    # Loop from 1 to n, including n
    for i in range(1, n + 1):
        # Print the current term
        print(t1)

        # Calculate the next term in the sequence
        result = t1 + t2

        # Update t1 and t2 for the next iteration
        t1 = t2
        t2 = result


if __name__ == "__main__":
    main()


def main():
    # Get input from the user
    n = int(input("Enter an integer (n): "))

    # Initialize the first two terms of the Fibonacci sequence
    t1, t2 = 1, 1

    # Run the loop as long as t1 is less than n
    while t1 < n:
        # Print the current term
        print(t1)

        # Calculate the next term in the sequence
        result = t1 + t2

        # Update t1 and t2 for the next iteration
        t1 = t2
        t2 = result


if __name__ == "__main__":
    main()