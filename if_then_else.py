def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def main():
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Factorial does not exist for negative numbers.")
        else:
            print(f"{factorial(num)}")
    except ValueError:
        print("Factorial does not exist for negative numbers.")


if __name__ == "__main__":
    main()
