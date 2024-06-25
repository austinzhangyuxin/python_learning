class NumberClassifier:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_even(self, number):
        return number % 2 == 0

    def classify(self):
        even_numbers = []
        odd_numbers = []
        for number in self.numbers:
            if self.is_even(number):
                even_numbers.append(number)
            else:
                odd_numbers.append(number)
        return even_numbers, odd_numbers

    def print_classification(self):
        even_numbers, odd_numbers = self.classify()
        print(f"Even numbers: {even_numbers}")
        print(f"Odd numbers: {odd_numbers}")


def get_numbers():
    user_input = input("Enter numbers (comma-separated for multiple, single number, or a range with '-'): ").strip()
    if ',' in user_input:
        numbers = list(map(int, user_input.split(',')))
    elif '-' in user_input:
        start, end = map(int, user_input.split('-'))
        numbers = list(range(start, end + 1))
    else:
        numbers = [int(user_input)]
    return numbers


def main():
    try:
        numbers = get_numbers()
        classifier = NumberClassifier(numbers)
        classifier.print_classification()
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid number or range.")


if __name__ == "__main__":
    main()
