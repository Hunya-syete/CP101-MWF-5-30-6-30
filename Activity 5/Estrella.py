strings = "HelloWorld! 123 #Python"

lowercase = 0
uppercase = 0
digits = 0
specialsymbol = 0 

for i in strings:
    if i.isupper():
        uppercase = uppercase + 1
    elif i.islower():
        lowercase += 1
    elif i.isdigit():
        digits += 1   
    else:
        specialsymbol += 1 

print("uppercase =",uppercase)
print("lowercase =",lowercase)
print("digits =",digits)
print("specialsymbol =",specialsymbol
