def count_characters(input_string):
    lower_case_count = 0
    upper_case_count = 0
    digit_count = 0
    special_symbol_count = 0
    
    for char in input_string:
        if char.islower():
            lower_case_count += 1
        elif char.isupper():
            upper_case_count += 1
        elif char.isdigit():
            digit_count += 1
        elif not char.isalnum():
            special_symbol_count += 1
    return {
        "lower_case": lower_case_count,
        "upper_case": upper_case_count,
        "digits": digit_count,
        "special_symbols": special_symbol_count,}
        
input_string = "I am Sid from BSIT-1 Block B SY:2024-2025 in St.Vincent College Incorporation"
result = count_characters(input_string)

print("Lowercase letters:", result["lower_case"])
print("Uppercase letters:", result["upper_case"])
print("Digits:", result["digits"])
print("Special symbols:", result["special_symbols"])
