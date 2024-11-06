def count_characters(s):
    counts = {'lowercase': 0, 'uppercase': 0, 'digits': 0, 'special': 0}
    
    for char in s:
        if char.islower():
            counts['lowercase'] += 1
        elif char.isupper():
            counts['uppercase'] += 1
        elif char.isdigit():
            counts['digits'] += 1
        else:
            counts['special'] += 1
            
    return counts

# Example usage
input_string = "Hello, World! 123"
print(count_characters(input_string))
You sent
def count_characters(s):
    counts = {'lowercase': 0, 'uppercase': 0, 'digits': 0, 'special': 0}
    
    for char in s:
        if char.is lower():
            counts['lowercase'] += 1
        elif char.isupper():
            counts['uppercase'] += 1
        elif char.isdigit():
            counts['digits'] += 1
        else:
            counts['special'] += 1
            
    return counts

# Example usage
input_string = "Hello, World! 123"
print(count_characters(input_string))
digitalassets.xyz
Sent
