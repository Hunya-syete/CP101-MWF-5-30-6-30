Character1 = input("Enter Text: ")

upperC = 0
lowerC = 0
digitC = 0
specialC = 0


for character in Character1:
    
    if character.isupper():
        
        upperC = upperC + 1
        
    elif character.islower():
        
        lowerC = lowerC + 1
        
    elif character.isdigit():
        
        digitC = digitC + 1
        
    else:
        
        specialC = specialC + 1
        

print(f"UPPERCASE: {upperC}")
print(f"LOWERCASE: {lowerC}")
print(f"DIGIT: {digitC}")
print(f"SPECIAL SYMBOLS: {specialC}")
