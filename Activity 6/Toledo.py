name = input("Enter your name: ")
age = input("Enter your age: ")
# Use an f-string to format the output
print(f"Hello,{name}! You are {age} years old. ")


item = "strawberry"
count = 6 
# Use the .format() method
sentence = "i bought {} {} today.".format(count, item)
print(sentence)


city = "Japan"
temperature = 24
# Use the % operator
print("The temperature in %s is %d degrees Celsius." % (city, temperature))
