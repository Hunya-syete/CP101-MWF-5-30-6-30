print("====") 
print("    ~ Record Keeping App ~")
print("====")
print("Available Operators:")
print("A) Add Data\t\tB) Delete Data")
print("C) End)")
selection = str(input("Select an option [A,B,C,]: "))

if selection.upper() =="A":
    var1 = str(input("Enter Lastname: "))
    var2 = str(input("Enter Firstname: "))
    file = open("record.txt", "a")
    file.write(f"\n{var1}, {var2},")
    file.close()
elif selection.upper() =="B":
    print("No records found.")
    file = open("record.txt", "r+")
    file.truncate(4)
    file.close()
elif selection.upper() == "C":
    print("Thank You Ma'am")
else:
    print("Invalid input.")
