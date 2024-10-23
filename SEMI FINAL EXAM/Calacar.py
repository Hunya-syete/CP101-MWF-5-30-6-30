#semi-finals exam for CP101-MWF-5:30-6:30PM
#author : Julius E. Calacar

print("====") 
print("    ~ Record Keeping App ~")
print("====")
print("Available Operators:")
print("A) Add Data\t\tB) Delete Data")
print("C) End)")
selection = str(input("Select an option [A,B,C,]: "))

if selection.upper() =="A":
    var11 = str(input("Enter Lastname: "))
    var22 = str(input("Enter Firstname: "))
    file = open("record.txt", "a")
    file.write(f"\n{var11}, {var22},")
    file.close(0)
elif selection.upper() =="B":
    print("No records found.")
    file = open("record.txt", "r+")
    file.truncate(0)
    file.close()
elif selection.upper() == "C":
    print(" Thank You ")
else:
    print("Invalid input.")
