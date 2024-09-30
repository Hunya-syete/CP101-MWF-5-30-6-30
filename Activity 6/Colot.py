# Create a Python code that solves the following exercises by applying the appropriate string formatting method:

name = input("Enter your name: ")
age = input("Enter your age: ")
# Use an f-string to format the output
print(f"Hello, {name}! You are {age} years old.")


item = "ballpen"
count = 10
# Use the .format() method
sentence = "I pick {} {} today.".format(count, item)
print(sentence)


city = "Dipolog City"
temperature = 28
# Use the % operator
print("The temperature in %s is %d degrees Celsius." % (city, temperature))

