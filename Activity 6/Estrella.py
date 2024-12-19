#Part 1: Basic f-string formatting 
Attempt = input("My name is: ") 
attempt2 = input("I like to play: ")
print(f"I am !{Attempt}, My habit is playing {attempt2}. nice to meet you")

print("\n")
#Part 2: using .format
Status = "single"
years = 65
variable1 = "I am currently {} and I want to be healthy even I am {} years old".format(years,years)
print(variable1)


print("\n")
#Part 3: Legacy % formatting.
term = "young"
years = 65
print("I want to be healthy if ever I will be %d years of age." % (term, years))
