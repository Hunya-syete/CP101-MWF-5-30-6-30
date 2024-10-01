sampleText1="My name is {}.I love {}. I love playing {}.{}"
sampleText1a=sampleText1.format("Khrisha","Watching vlog","Badminton","Orange")

print(sampleText1a)

sampleText2= "My name is {1}.I love {2}.I love playing {0}."
sampleText2a= sampleText2.format("Badminton","Khrisha","Watching vlog","Orange")
print(sampleText2a)
sampleText3= "My name {name}.I love {food}. I love playing {play}." 
sampleText3a= sampleText3.format(food="eating fluffy food",play="Badminton",name="Khrisha")
print(sampleText3a)
