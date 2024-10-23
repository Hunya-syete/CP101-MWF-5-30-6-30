# Part 1: Basic f-string Formatting 
Attempt = input("My name is: ") 
attempt2 = input("I am inspired of: ")
print(f"Hi everybody I want to introduce my self to you I am !{Attempt}, I have many things to know about {attempt2}. Thank You!")

print("\n")
#Part 3: Legacy % formatting.
Status = "Poor"
Money_left = 5
variable1 = "The life are so unfair, basically I am {} right now, I only have {} pesos huhu Ginoo Ko!".format( Status,Money_left)
print(variable1)


print("\n")
#Part 3: Legacy % formatting.
again = "cash"
total = 99000
print(" I lost a %s somewhere and it cost a toal of %d." % (again, total))
