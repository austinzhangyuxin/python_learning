year = 2000

# if divisible by 400, it"s a leap year
if year % 400 == 0:
    result = "leap year"

# at this point, we know it"s not divisible by 400
# if it"s divisible by 100, it"s not a leap year
elif year % 100 == 0:
    result = "not a leap year"

# at this point we know it"s not a century year
# if a non-century year is divisible by 4, it"s a leap year
elif year % 4 == 0:
    result = "leap year"

# all other remaining years are not a leap year
else:
    result = "not a leap year"

print(result)
# -----------------------------------------------------------------------
year = 2000

# if year is divisible by 4 and not divisible by 100
# or if year is divisible by 400, it"s a leap year
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    result = "leap year"

# all other remaining years are not a leap year
else:
    result = "not a leap year"

print(result)


# -----------------

def is_leap_year(year):
    """
    Check if a given year is a leap year.
    Leap year rules:
    - Divisible by 4, except for years divisible by 100 unless also divisible by 400.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def count_leap_years(start_year, end_year):
    """
    Count the number of leap years between start_year and end_year (inclusive).
    """
    leap_year_count = 0
    for year in range(start_year, end_year + 1):
        if is_leap_year(year):
            leap_year_count += 1
    return leap_year_count


def main():
    print("Welcome to the Advanced Leap Year Checker!")

    try:
        start_year = int(input("Enter the starting year: "))
        end_year = int(input("Enter the ending year: "))

        if start_year > end_year:
            print("Invalid range. Starting year must be less than or equal to ending year.")
            return

        # Display leap years within the range
        print(f"\nLeap years between {start_year} and {end_year}:")
        for year in range(start_year, end_year + 1):
            if is_leap_year(year):
                print(year)

        # Count leap years within the range
        leap_year_count = count_leap_years(start_year, end_year)
        print(f"\nTotal number of leap years between {start_year} and {end_year}: {leap_year_count}")

    except ValueError:
        print("Invalid input. Please enter valid integer years.")


if __name__ == "__main__":
    main()
