# Replace ___ with your code

# get input value for total number of friends
total_friends = int(input("total number of friends: "))

# get input value for total bill
total_bill = float(input("bill: "))

# calculate the tax amount
tax = total_bill * 20 / 100
print(f'tax: {tax}')

# divide bill among friends
total_bill = total_bill + tax

# print the split amount
print(total_bill / total_friends)


# --------------------------------------
class Child:
    def __init__(self, name):
        self.name = name
        self.amount_to_pay = 0.0


class BillSplitter:
    def __init__(self):
        self.children = []
        self.bills = {}

    def add_child(self, child_name):
        self.children.append(Child(child_name))

    def add_bill(self, bill_category, bill_amount):
        if bill_category not in self.bills:
            self.bills[bill_category] = bill_amount
        else:
            self.bills[bill_category] += bill_amount

    def calculate_share(self):
        total_amount = sum(self.bills.values())
        if not self.children:
            raise ValueError("No children added for splitting")

        share_per_child = total_amount / len(self.children)
        for child in self.children:
            child.amount_to_pay = share_per_child

    def print_report(self):
        if not self.bills:
            print("No bills added.")
            return

        print("Bill Summary:")
        for category, amount in self.bills.items():
            print(f"{category}: ${amount:.2f}")

        print("\nPayment Details:")
        for child in self.children:
            print(f"{child.name}: ${child.amount_to_pay:.2f}")


def main():
    print("Welcome to the Advanced Bill Splitting Project!")
    splitter = BillSplitter()

    try:
        num_children = int(input("Enter number of children: "))
        for i in range(1, num_children + 1):
            child_name = input(f"Enter name of child {i}: ")
            splitter.add_child(child_name)

        while True:
            bill_category = input("Enter bill category (type 'done' to finish): ").strip().lower()
            if bill_category == 'done':
                break
            bill_amount = float(input("Enter bill amount: $"))
            splitter.add_bill(bill_category, bill_amount)

        splitter.calculate_share()
        splitter.print_report()

    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()
