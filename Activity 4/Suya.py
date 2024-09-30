sampleText1a = sampleText1.format("Christian", "Ice Cream", "Volleyball", "lanzones")
print(sampleText1a)

sampleText2 = "My name is {1}. I love {2}. I love playing {0}."
sampleText2a = sampleText2.format("Basketball", "Christian", "Ice Cream", "Volleyball", "lanzones")
print(sampleText2a)

sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(play="Burger", name="Christian", food="Ice Cream"

item = "squash"
cost = 39.0
SampleText4 = "The product is %s the cost is %.5f." % (item, cost)
print(SampleText4)

item = "squash"
cost = 1500

SampleText5 = f"The item is {item} and the cost is {cost * 100} pesos."
print(SampleText5)
