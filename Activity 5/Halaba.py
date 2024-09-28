findChar = {"uppercase" : 0, "lowercase" : 0, "numeric" : 0, "special" : 0}

strings = "Hello World! 123 # Python"


for character in strings:
    if character.isupper():
        findChar["uppercase"] += 1
    if character.islower():
        findChar["lowercase"] += 1
    if character.isupper():
        findChar["numeric"] += 1
    if not character.isalnum() and character.find(" "):
        findChar["special"] += 1

for x in findChar:
    res = findChar.get(x)
    print(f"The number of {x} is :{res:>3}")
