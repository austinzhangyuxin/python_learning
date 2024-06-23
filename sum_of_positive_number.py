# the initial value of total is 0
total = 0

while True:

    number = int(input("Enter a number: "))

    # if number is negative, don't add that number to total
    if number < 0:
        continue

    # if number is zero, terminate the loop
    if number == 0:
        break

    total = total + number

print(f"Total: {total}")