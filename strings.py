# Creating strings
name = "Alice"
message = 'Hello, World!'
empty_string = ""
multiline_string = """This is a
multiline string"""

# Accessing characters in a string
print(name[0])  # Output: 'A' (accessing first character)
print(message[7])  # Output: 'W' (accessing character at index 7)

# String length
print(len(message))  # Output: 13 (length of the string)

# String slicing
print(message[0:5])  # Output: 'Hello' (slicing from index 0 to 4)
print(message[7:])  # Output: 'World!' (slicing from index 7 to end)

# Concatenating strings
greeting = "Hello"
name = "Alice"
welcome_message = greeting + ", " + name + "!"  # Output: 'Hello, Alice!'

# String repetition
print(name * 3)  # Output: 'AliceAliceAlice'

# String methods
print(message.lower())  # Output: 'hello, world!' (converts string to lowercase)
print(message.upper())  # Output: 'HELLO, WORLD!' (converts string to uppercase)
print(message.split())  # Output: ['Hello,', 'World!'] (splits string into a list of words)
print(message.startswith('Hello'))  # Output: True (checks if string starts with 'Hello')
print(message.endswith('!'))  # Output: True (checks if string ends with '!')

# String formatting
age = 30
formatted_message = f"My name is {name} and I am {age} years old."  # Using f-string
print(formatted_message)  # Output: 'My name is Alice and I am 30 years old.'

# Escape characters
escaped_string = "This is a \"quote\" inside a string."
print(escaped_string)  # Output: 'This is a "quote" inside a string.'

# Multiline strings
multiline_string = """This is a
multiline string"""
print(multiline_string)
# --------------------
# Assign the string "Snowpiercer" to the variable movie
movie = "Snowpiercer"

# Print the fourth character from the string (using a positive index)
# Remember, indexing starts at 0, so the fourth character is at index 3
print(movie[3])  # Output: 'w'
# -----------------------
# Get two string inputs from the user
text1 = input("Enter the first string: ")
text2 = input("Enter the second string: ")

# Create a new string with the first four characters of text1 and the last four characters of text2
result = text1[:4] + text2[-4:]

# Print the resultant string
print(result)