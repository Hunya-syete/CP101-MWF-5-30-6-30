
rate = 0
hours = 0

class work_rate:
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate(self):
        return self.hours * self.rate


while not ValueError or hours <= 0:
    hours = input("Whats your hours: ")
    try:
        hours = float(hours)
        if hours <= 0:
            print(f"Value should not be equal to or less than 0 \"{hours}\"")
    except ValueError:
            print("Numerical numbers only")

while not ValueError or rate <= 0:
    rate = input("Whats your rate: ")
    try:
        rate = float(rate)
        if rate <= 0:
            print(f"Value should not be equal to or less than 0 \"{rate}\"")
    except ValueError:
            print("Numerical numbers only")


user = work_rate(hours, rate)
result = work_rate.calculate((user))


print(f"Your gross pay is: {result}")

