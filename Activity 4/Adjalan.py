sampleText1 = "My name is {}. I love {}. I love playing {}. {}"
sampleText1a = sampleText1.format("Rayhana", "Watching Videos", "8 ball" , "Mango")

print(sampleText1a)


sampleText2 = "My name is {1}. I love {2}. I love playing {0}."
sampleText2a = sampleText2.format("8 ball", "Rayray", "Watching Videos", "8 ball", "Cake")
print(sampleText2a)

sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(food="Ice cream", play="8 ball", name="Rayhana")
print(sampleText3a)
