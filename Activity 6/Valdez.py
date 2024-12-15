# Rustom Carl M. Valdez BSIT (5:30 - 6:30)

# Part 1: Basic f-string Formatting 
pangalan = input("Enter your pangalan: ")
edad = input("Enter your edad: ")
print(f"Hello, {pangalan}! You are {edad} years old.")

# Part 2: Using  .format()
count = 3
item = "Red Bull"
sentence = "I bought {} {} today.".format(count, item)
print(sentence)

# Part 3: Legacy % formatting.
city = "Philippines"
temperature = 40.3
print("The temperature in %s is %.1f degrees Celsius." % (city, temperature))
