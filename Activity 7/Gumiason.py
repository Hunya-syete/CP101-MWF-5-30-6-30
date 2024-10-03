#Gumiason.python coding: program that will check a worker years of service an office.

Course = input("Chose your graduated course(IT, ACC or HM?): ")
Years = int(input("How many year have you worked?: "))

if Course == "IT":
    if Years >= 10:
        Pay = 10000
    elif Years < 10:
        Pay = 5000
        
if Course == "ACC":
    if Years >= 10:
        Pay = 12000
    elif Years < 10:
        Pay = 6000
 
if Course == "HM":
    if Years >= 10:
        Pay = 15000
    elif Years < 10:
        Pay = 7500
        
print("Your years of service is cost", Pay)




