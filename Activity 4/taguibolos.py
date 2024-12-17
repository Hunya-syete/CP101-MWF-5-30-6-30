sampleText1 = "My name is {}. I love {}. I love playing {}."
sampleText1a = sampleText1.format("jay", "Travelling", "ML")
print(sampleText1a)

sampleText2 = "My name is {1}. I love {2}. I love playing {0}."
sampleText2a = sampleText2.format("ML", "jay", "Travelling")
print(sampleText2a)

sampleText3 = "My name is {name}. I love {hobby}. I love playing {play}."
sampleText3a = sampleText3.format(hobby="Travelling", play="ML", name="jay")
print(sampleText3a)
