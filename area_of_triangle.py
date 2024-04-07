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