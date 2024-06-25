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


# --------------------------

def generate_multiplication_table(rows, cols):
    # Print header row
    header = "     |"
    for col in range(1, cols + 1):
        header += f" {col:4}"
    print(header)
    print("-" * (len(header)))

    # Print table rows
    for row in range(1, rows + 1):
        line = f" {row:3} |"
        for col in range(1, cols + 1):
            line += f" {row * col:4}"
        print(line)


def main():
    print("Welcome to the Advanced Multiplication Table Generator!")
    print("Enter the range for the table (1 to n):")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    generate_multiplication_table(rows, cols)


if __name__ == "__main__":
    main()
