sampleText1 = "My name is {}. I love {}. I love playing {}. {}"
sampleText1a = sampleText1.format("Hyacinth", "Watching tiktok", "8 ball" , "Banana")

print(sampleText1a)


sampleText2 = "My name is {1}. I love {2}. I love playing {0}."
sampleText2a = sampleText2.format("8 ball", "Hya", "Watching Videos", "8 ball", "Apple")
print(sampleText2a)

sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(food="Fries", play="8 ball", name="Cinth")
print(sampleText3a)
