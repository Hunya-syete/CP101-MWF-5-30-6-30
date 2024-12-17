#sampleText1 = "My name is {}. I love {}. I love playing {}. {}"
#sampleText1a = sampleText1.format("Rustom Carl", "Burger", "Racing", "Shooting")
#print(sampleText1a)



#sampleText2 = "My name is {1}. I love {2}. I love playing {0}."
#sampleText2a = sampleText2.format("COD", "Rustom Carl", "Burger", "Racing", "Shooting")
#print(sampleText2a)



#sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
#sampleText3a = sampleText3.format(food="Burger", play="COD", name="Rustom Carl")
#print(sampleText3a)

#item = "Milk"
#cost = 35.5
#SampleText4 = "The product is %s the cost is %.2f." % (item, cost)
#print(SampleText4) 

item = "Custom PC Build"
cost = 900

SampleText5 = f"The item is {item} and the cost is {cost * 100} pesos."
print(SampleText5)  
