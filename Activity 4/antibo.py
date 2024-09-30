sampleText1 = "My name is {}. I love {}. I love playing {}. {}"
sampleText1a = sampleText1.format("Madelyn", "Watching Tiktok", "Zombiee Catcher" , "Grapes")

print(sampleText1a)


sampleText2 = "My name is {1}. I love {2}. I love playing {0}."
sampleText2a = sampleText2.format("Playing Badminton", "Madelyn", "Watching Videos", "Zombee Catcher", "Grapes")
print(sampleText2a)

sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(food="Humburger", play="Zombee Catcher", name="Madelyn")
print(sampleText3a)
