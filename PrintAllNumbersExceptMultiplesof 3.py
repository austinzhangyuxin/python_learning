def main():
    # Get input from the user
    n = int(input("Enter an integer (n): "))

    # Loop from 1 to n
    for i in range(1, n + 1):
        # Check if i is divisible by 3
        if i % 3 == 0:
            continue  # Skip the current iteration

        # Print the value of i
        print(i)


if __name__ == "__main__":
    main()