
# math =    95
# science = 80
# english = 92

subjects = ["Math", "English", " Science"]
grades = []
add = 0
i = 0

while not len(grades) == len(subjects):
    grade = input(f"Write your {subjects[i]} grade: ")
    try:
        grade = float(grade)
        if grade <= 0:
            print("Value is less than or equal to 0 ")
        else:
            grades.append(grade)
            i += 1
    except ValueError:
        print("Numerical numbers only")


for x in range(len(subjects)):
    add += grades[x]

average = add/len(subjects)

print(f"Average: {average}")
