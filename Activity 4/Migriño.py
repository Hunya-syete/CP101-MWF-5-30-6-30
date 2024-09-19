sampleText1 = "My name is {}. I love {}. I love playing {}."
sampleText1a = sampleText1.format("Sid", "Travelling", "Dota 2")
print(sampleText1a)

sampleText2 = "My name is {1}. I love {2}. I love playing {0}."
sampleText2a = sampleText2.format("Dota 2", "Sid", "Travelling")
print(sampleText2a)

sampleText3 = "My name is {name}. I love {hobby}. I love playing {play}."
sampleText3a = sampleText3.format(hobby="Travelling", play="Dota 2", name="Sid")
print(sampleText3a)
