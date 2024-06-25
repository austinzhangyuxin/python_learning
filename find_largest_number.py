def get_largest_number(n1, n2, n3):
    # return n1 if it's the largest number
    if n1 >= n2 and n1 >= n3:
        return n1

    # return n2 if it's the largest number
    elif n2 >= n1 and n2 >= n3:
        return n2

    # else return n3
    else:
        return n3


largest_number = get_largest_number(3, 55, -5)
print(largest_number)  # Output: 55

largest_number = get_largest_number(0, 12, 20)
print(largest_number)  # Output: 20


def get_largest_number(n1, n2, n3):
    # n1 is the largest
    if n1 >= n2 and n1 >= n3:
        largest_number = n1

    # n2 is the largest
    elif n2 >= n1 and n2 >= n3:
        largest_number = n2

    # else return n3
    else:
        largest_number = n3

    return largest_number


largest_number = get_largest_number(3, 55, -5)
print(largest_number)  # Output: 55

largest_number = get_largest_number(0, 12, 20)
print(largest_number)  # Output: 20