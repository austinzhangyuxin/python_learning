# get three sides of the triangle from the user
# store them in variables a, b, and c
a = float(input("value of a: "))
b = float(input("value of b: "))
c = float(input("value of c: "))
# compute semiperimeter s, s = (a+b+c)/2
s = (a + b + c)/2

# compute area and print it
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"Area of triangle with sides {a}, {b} and {c} is {area}.")

# Replace ___ with your code

# take input for base and height
base =float(input("base: "))
height = float(input("height: "))

# calculate the area
area =1/2 * base * height
# print area
print (area)

import math


def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area


def calculate_triangle_area_heron(side1, side2, side3):
    # Calculate semi-perimeter
    s = (side1 + side2 + side3) / 2
    # Calculate area using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area


def main():
    print("Welcome to the Advanced Triangle Area Calculator!")
    while True:
        try:
            print("\nChoose the type of triangle you want to calculate:")
            print("1. Right Triangle (Base and Height)")
            print("2. Scalene Triangle (Three Sides)")
            print("3. Equilateral Triangle (Side Length)")
            print("4. Exit")

            choice = int(input("Enter your choice (1/2/3/4): "))

            if choice == 1:
                base = float(input("Enter the base length of the right triangle: "))
                height = float(input("Enter the height of the right triangle: "))
                if base <= 0 or height <= 0:
                    print("Base and height should be positive numbers.")
                else:
                    area = calculate_triangle_area(base, height)
                    print(
                        f"The area of the right triangle with base {base} and height {height} is: {area:.2f} square units.")

            elif choice == 2:
                side1 = float(input("Enter the length of side 1 of the scalene triangle: "))
                side2 = float(input("Enter the length of side 2 of the scalene triangle: "))
                side3 = float(input("Enter the length of side 3 of the scalene triangle: "))
                if side1 <= 0 or side2 <= 0 or side3 <= 0:
                    print("Side lengths should be positive numbers.")
                else:
                    area = calculate_triangle_area_heron(side1, side2, side3)
                    print(
                        f"The area of the scalene triangle with sides {side1}, {side2}, {side3} is: {area:.2f} square units.")

            elif choice == 3:
                side = float(input("Enter the length of the side of the equilateral triangle: "))
                if side <= 0:
                    print("Side length should be a positive number.")
                else:
                    area = (math.sqrt(3) / 4) * side ** 2
                    print(f"The area of the equilateral triangle with side {side} is: {area:.2f} square units.")

            elif choice == 4:
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

        except ValueError:
            print("Invalid input. Please enter valid numerical values.")


if __name__ == "__main__":
    main()
