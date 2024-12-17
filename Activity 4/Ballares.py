sampleText1 = "My name is {}. I love {}. I love playing {}. {}"
sampleText1a = sampleText1.format("Aldrin", "Watching Videos", "Mobile Legends" , "Apple")

print(sampleText1a)


sampleText2 = "My name is {1}. I love {2}. I love playing {0}."
sampleText2a = sampleText2.format("Puzzle", "Aldrin", "Watching Videos", "Mobile Legends", "Apple")
print(sampleText2a)

sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(food="Fries", play="Mobile legends", name="Aldrin")
print(sampleText3a)
