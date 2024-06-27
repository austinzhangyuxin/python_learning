def main():
    # Get input from the user
    n = int(input("Enter an integer (n): "))

    total_sum = 0

    # Loop from 1 to n
    for i in range(1, n + 1):
        # Calculate the sum of numbers from 1 to i
        total_sum += i

    # Print the result
    print(f"{total_sum}")

if __name__ == "__main__":
    main()
