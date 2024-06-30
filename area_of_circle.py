def compute_area(radius, pi):
    """
    Function to compute the area of a circle.
    """
    area = pi * (radius ** 2)
    return area


def main():
    # Get a float input value for the radius of the circle
    radius = float(input("Enter the radius of the circle: "))

    # Create a float variable named pi with value 3.14
    pi = 3.14

    # Call compute_area function with arguments radius and pi
    area_of_circle = compute_area(radius, pi)

    # Print the returned value
    print(f"The area of the circle with radius {radius} is: {area_of_circle}")


if __name__ == "__main__":
    main()

