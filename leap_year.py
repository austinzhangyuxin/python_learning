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
