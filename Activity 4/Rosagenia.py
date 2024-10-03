sampleText1 = "My name is {}. I love {}. I love playing {}."
sampleText1a = sampleText1.format("John Renz","Money", "Mobile Legends")
print(sampleText1a)

sampleText2 = "My name is {0}. I love {1}. I love playing {2}."
sampleText2a = sampleText2.format("John Renz", "Scatter","Mobile Legends")
print(sampleText2a)


sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(food="Money", play="Mobile Legends", name="John Renz")
print(sampleText3a)

item = "milk"
cost = 35.5
SampleText4 = "The product is %s and the cost is %.5f." % (item, cost)  # Use the variables, not their names
print(SampleText4)

item = "apple watch" 
cost = 9900
SampleText5 = f"The item is {item} and the cost is {cost * 100} pesos."
print(SampleText5)
