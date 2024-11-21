Job = input("IT, ACC or HR?: ")
Years = int(input("How many year have you worked?: "))

if Job == "IT":
    if Years >= 10:
        Pay = 10000
    elif Years < 10:
        Pay = 5000
       
elif Job == "ACC":
    if Years >= 10:
        Pay = 12000
    elif Years < 10:
        Pay = 6000
 
elif Job == "HR":
    if Years >= 10:
        Pay = 15000
    elif Years < 10:
        Pay = 7500
       
print(Pay)
