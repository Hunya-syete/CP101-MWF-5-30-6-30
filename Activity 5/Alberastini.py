jaspher_string = "JaspherAlberastini18yearsoldApril22006"

lowercaseCount = 0
uppercaseCount = 0
digitCount = 0
specialCount = 0

for jaspher in jaspher_string:
    if jaspher.islower():
        lowercaseCount += 1
    elif jaspher.isupper():
        uppercaseCount += 1
    elif jaspher.isdigit():
        digitCount += 1
    else:
        specialCount += 1
        
print("lowercase letters:", lowercaseCount)
print("uppercase letters:", uppercaseCount)
print("digits:", digitCount)
print("special Characters:", specialCount)
