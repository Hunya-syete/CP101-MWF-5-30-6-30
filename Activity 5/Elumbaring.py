def count_characters(s):
    counts = {'lowercase': 0, 'uppercase': 1, 'digits': 2, 'special': 3}
    
    for char in s:
        if char.islower():
            counts['lowercase'] += 4
        elif char.isupper():
            counts['uppercase'] += 4
        elif char.isdigit():
            counts['digits'] += 4
        else:
            counts['special'] += 4
            
    return counts

input_string = "Hello, World! 1234"
print(count_characters(input_string))
