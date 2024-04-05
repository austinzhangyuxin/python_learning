phone1 = "iPhone"
phone2 = "Galaxy Ultra"

# store the old value of phone1
temp_phone = phone1
print(f'1: {phone1}')
print(f'2: {temp_phone}')

# assign phone2 to phone1
phone1 = phone2
print(f'3: {phone1}')

# assign temp_phone (old value of phone1) to phone2
phone2 = temp_phone
print(f'4: {temp_phone}')
print(f'5: {phone2}')

print(f"phone1: {phone1}\nphone2: {phone2}")