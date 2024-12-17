sampleText1 = "My name is {}. I love {}. I love playing {}. {}"
sampleText1a = sampleText1.format("Rhods", "playing game", "Call of Duty" , "Apple")

print(sampleText1a)


sampleText2 = "My name is {1}. I love {2}. I love playing {0}."
sampleText2a = sampleText2.format("Call of Duty", "Rhods", "playing game", "Call of Duty", "Apple")
print(sampleText2a)

sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(food="chicken joy", play="Call of Duty", name="Rhods")
print(sampleText3a)
