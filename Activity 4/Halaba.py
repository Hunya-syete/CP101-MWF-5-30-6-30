sampleText1 = "My name is {}. I love {}. I love playing {}"
sampleText1a = sampleText1.format("Clifford", "Henriet", "Boxing")
print(sampleText1a)


sampleText2 = "My name is {1}. I love {2}. I love playing {0}."
sampleText2a = sampleText2.format("Boxing", "Clifford", "Henriet", "Ros", "Borgarr")
print(sampleText2a)

sampleText3 = "My name is {name}. I love {her}. I love playing {play}."
sampleText3a = sampleText3.format(her="Henriet", play="Boxing", name="Clifford")
print(sampleText3a)
