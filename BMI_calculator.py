
# take float input for weight
weight =float(input("weight in kg: "))

# take float input for height
height =float(input("height in meters: "))

# calculate BMI
BMI = weight / height**2

# print the calculated BMI
print(BMI)


def calculate_bmi(weight, height, system='metric'):
    if system == 'metric':
        bmi = weight / (height ** 2)
    elif system == 'imperial':
        bmi = (weight / (height ** 2)) * 703
    else:
        raise ValueError("Invalid measurement system. Please choose 'metric' or 'imperial'.")

    return bmi


def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def bmi_calculator():
    print("Welcome to the BMI Calculator!")
    while True:
        try:
            system = input("Choose measurement system (metric/imperial): ").lower()
            if system not in ['metric', 'imperial']:
                print("Invalid input. Please enter 'metric' or 'imperial'.")
                continue

            weight = float(input(f"Enter your weight in {'kilograms' if system == 'metric' else 'pounds'}: "))
            height = float(input(f"Enter your height in {'meters' if system == 'metric' else 'inches'}: "))

            bmi = calculate_bmi(weight, height, system)
            bmi_category = interpret_bmi(bmi)

            print(f"Your BMI is: {bmi:.2f}")
            print(f"You are categorized as: {bmi_category}\n")

            choice = input("Do you want to calculate again? (yes/no): ").lower()
            if choice != 'yes' and choice != 'y':
                break
        except ValueError:
            print("Invalid input. Please enter valid numerical values.")


if __name__ == "__main__":
    bmi_calculator()
