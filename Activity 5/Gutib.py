# Function to count different character types
def count_characters(s):
    lower_case = sum(1 for char in s if char.islower())
    upper_case = sum(1 for char in s if char.isupper())
    digits = sum(1 for char in s if char.isdigit())
    special_symbols = sum(1 for char in s if not char.isalnum())
    
    return lower_case, upper_case, digits, special_symbols

# Input string
input_string = input("Enter a string: ")

# Count the characters
lower, upper, digits, special = count_characters(input_string)

# Display results
print(f"Lowercase letters: {lower}")
print(f"Uppercase letters: {upper}")
print(f"Digits: {digits}")
print(f"Special symbols: {special}")
