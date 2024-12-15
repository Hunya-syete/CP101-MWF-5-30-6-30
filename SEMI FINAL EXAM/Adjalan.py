print("Record Keeping App")
print("Choose an Options:")
print("(Add Data, Delete Data, End)")
print()
selection = str(input("Select an option [1,2,3]: "))

if selection.upper() == "1":
    var1 = str(input("Enter Key: "))
    var2 = str(input("Enter Value: "))
    print("Your Officially added")
elif selection.upper() == "2":
    var1 = str(input("Enter Key:"))
    print("Your Now Officially Remove")
    
elif selection.upper() == "3":
    print("Thank you")
else:
    print("Invalid input.")
