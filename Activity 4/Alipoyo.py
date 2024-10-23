sampleText1 = "My name is {}. I love {}. I love playing {}."
sampleText1a = sampleText1.format("Ivann","Pizza", "Frisbee")
print(sampleText1a)

sampleText2 = "My name is {0}. I love {1}. I love playing {2}."
sampleText2a = sampleText2.format("Ivann", "Pizza","Frisbee")
print(sampleText2a)


sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(food="Pizza", play="Frisbee", name="Ivann")
print(sampleText3a)
