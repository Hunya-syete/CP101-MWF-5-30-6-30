input_string = input("Enter a string: ")

lower_case = sum(1 for char in input_string if char.islower())
upper_case = sum(1 for char in input_string if char.isupper())
digits = sum(1 for char in input_string if char.isdigit())
special_symbols = len(input_string) - (lower_case + upper_case + digits)

print(f"Lowercase letters: {lower_case}")
print(f"Uppercase letters: {upper_case}")
print(f"Digits: {digits}")
print(f"Special symbols: {special_symbols}")
