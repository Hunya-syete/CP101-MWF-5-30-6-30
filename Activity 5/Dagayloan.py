def count_characters(input_string):
    counts = {
        'lowercase': 0,
        'uppercase': 0,
        'digits': 0,
        'special_symbols': 0
    }
    
    for char in input_string:
        if char.islower():
            counts['lowercase'] += 1
        elif char.isupper():
            counts['uppercase'] += 1
        elif char.isdigit():
            counts['digits'] += 1
        elif not char.isspace():  
            counts['special_symbols'] += 1
            
    return counts

input_str = "Python 3.9 is fun!"
result = count_characters(input_str)
print(result)
