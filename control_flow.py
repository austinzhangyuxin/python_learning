numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
threshold = 7

for number in numbers:
    if number % 2 != 0:
        continue

    while True:
        if number > threshold:
            break
        else:
            print(number)
            break

