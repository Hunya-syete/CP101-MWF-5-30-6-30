Text = "JOAfil 123 @$$"

U = 0
L = 0
D = 0
S = 0

for C in Text:
    if C.isupper():
        U += 1
       
    elif C.islower():
        L += 1
        
    elif C.isdigit():
        D += 1
        
    else:
        S += 1
       
print("No. of Upper Case Letters: ", U)
print("No. of Lower Case Letters: ", L)
print("No. of Digits: ", D)
print("No. of Special Symbols: ", S)
        
        


# Anthony Joafil F. Crusante BSIT(1)B
