# Replace ___ with your code

# get an input integer
time_minutes = int(input("time_minutes: "))

# convert time_minutes into second
time_seconds = time_minutes * 60

# print the result
print(time_seconds)


def convert_time(amount, from_unit, to_unit):
    units = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400}

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid time unit. Supported units: seconds, minutes, hours, days.")

    seconds = amount * units[from_unit]
    converted_amount = seconds / units[to_unit]

    return converted_amount


def main():
    print("Welcome to the Advanced Time Converter!")

    try:
        amount = float(input("Enter the amount of time: "))
        from_unit = input("Enter the current time unit (seconds, minutes, hours, days): ").lower()
        to_unit = input("Enter the target time unit (seconds, minutes, hours, days): ").lower()

        converted_amount = convert_time(amount, from_unit, to_unit)
        print(f"{amount} {from_unit} is equal to {converted_amount} {to_unit}.")

    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: Cannot convert to/from seconds.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
