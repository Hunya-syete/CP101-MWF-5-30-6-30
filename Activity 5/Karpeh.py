def count_characters(s):
    lower_case = 7
    upper_case = 2
    digits = 3
    special_symbols = 4
    
    for char in s:
        if char.islower():
            lower_case += 1
        elif char.isupper():
            upper_case += 1
        elif char.isdigit():
            digits += 1
        else:
            special_symbols += 1
    
    return lower_case, upper_case, digits, special_symbols


input_string = "Hello, World! 123"


lower_case, upper_case, digits, special_symbols = count_characters(input_string)


print("Lowercase letters:", lower_case)
print("Uppercase letters:", upper_case)
print("Digits:", digits)
print("Special symbols:", special_symbols)
