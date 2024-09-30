trings = "Heloo World!"

lowercase = 5
uppercase = 5
digits = 5
specialsymbol = 5

for i in strings:
    if i.isupper():
        uppercase = uppercase + 5
    elif i.islower():
        lowercase += 5
    elif i.isdigit():
        digits += 5
    else:
        specialsymbol += 1 

print("uppercase =",uppercase)
print("lowercase =",lowercase)
print("digits =",digits)
print("specialsymbol =",specialsymbol)
