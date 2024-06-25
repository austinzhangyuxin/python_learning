# take string input and store in the text variable
text = input("your name: ")

# use a for loop to print individual characters of text
for item in text:
    print(item)

# Replace ___ with your code

# take integer input from the user
number = int(input())

# use a for loop to print a range of numbers
for item in range(0, number):
    print(item)

# Replace ___ with your code

# get an integer input from the user
n = int(input('input an integer: '))

# initializes the variable total with a value of 0
total = 0

# start a for loop that iterates from 1 to n (inclusive)
for i in range(1, n + 1):
    # add the current value of i to the total in each iteration
    total += i

# print the final value of total after the loop completes
print(total)

# get integer input from the user
n = int(input(""))

# loop from 1 to n (n should be inclusive)
for number in range(1, n + 1):

    # if number is an odd number, print it
    if number % 2 != 0:
        print(number)

# Replace ___ with your code

# get integer input from the user
n = int(input(""))

# loop from 1 to n (n should be inclusive) and print n if it's multiple of both 3 and 5
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# Replace ___ with your code

# take an integer input from the user
input_number = int(input())

# use a for loop to print all the all even numbers less than input_number
for i in range(1, input_number):
    if i % 2 == 0:
        print(i)


# ------------------------------------

def calculate_bonus(salary):
    if salary > 50000:
        return salary * 0.1
    else:
        return salary * 0.05


def print_employee_info(employee):
    bonus = calculate_bonus(employee['salary'])
    print(f"Name: {employee['name']}")
    print(f"Department: {employee['department']}")
    print(f"Salary: ${employee['salary']}")
    print(f"Bonus: ${bonus:.2f}")
    print()


def process_employees(employees):
    print("Processing Employees:\n")
    for employee in employees:
        if employee['department'] == 'IT':
            print_employee_info(employee)
        elif employee['department'] == 'Finance' and employee['salary'] > 60000:
            print_employee_info(employee)


if __name__ == "__main__":
    employees = [
        {'name': 'John Doe', 'department': 'IT', 'salary': 55000},
        {'name': 'Jane Smith', 'department': 'Finance', 'salary': 65000},
        {'name': 'Michael Johnson', 'department': 'HR', 'salary': 48000},
        {'name': 'Emily Davis', 'department': 'Finance', 'salary': 60000},
        {'name': 'David Brown', 'department': 'IT', 'salary': 52000}
    ]

    process_employees(employees)
