department = {"IT" : [5000, 10000],
              "AC" : [6000, 12000],
              "HR" : [7500, 15000]}
questions = ["whats the department? :", 
             "Ammount of years: "]



class jobwage:
    def __init__(self, department, years):
        self.depar = department
        self.years = years

    def cheak(self):
        for key in department.keys():
            if self.depar == key:
                wages = department.get(self.depar)

        for wage in wages:
            if wage == wages[0] and not self.years >= 10:
                return wage
            if wage == wages[1] and self.years >= 10:
                return wage
            


print("select your department:")
for key in department.keys():
    print(key, end=" ")
print()

depar = input(questions[0])
years = input(questions[1])

depar = depar.upper()
years = int(years)

res = jobwage(depar, years)
res = jobwage.cheak(res)
print(f"Result of {key} job with the {years} year/s is: {res}")
