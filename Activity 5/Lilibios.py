strings = "Hello World! 123 #Python"

lower_case = 0
upper_case = 0
digits = 0
special_symbols = 0

for string in strings:
    if string.islower():
      lower_case = lower_case + 1
    elif string.isupper():
        upper_case = upper_case + 1
    elif string.isdigit():
        digits = digits + 1
    else:
        special_symbols = special_symbols + 1

print("Lowercase:",lower_case)
print("Uppercase:",upper_case)
print("Digits:",digits)
print("Special Symbols:",special_symbols)
