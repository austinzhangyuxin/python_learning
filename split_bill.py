# Replace ___ with your code

# get input value for total number of friends
total_friends = int(input("total number of friends: "))

# get input value for total bill
total_bill =float(input("bill: "))

# calculate the tax amount
tax = total_bill * 20/100
print(f'tax: {tax}')

# divide bill among friends
total_bill = total_bill + tax

# print the split amount
print(total_bill/total_friends)