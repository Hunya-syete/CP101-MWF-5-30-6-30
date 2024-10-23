grades = [float(input(f"Enter your {subject} grade: ")) for subject in ["Math", "English", "Science"]]
print(f"Average grade: {sum(grades)/3:.2f}")
