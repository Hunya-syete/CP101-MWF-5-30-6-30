Vault = {}

print("A. Add Data")
print("B. Delete Data")
print("C. End")

while True:
    print(Vault)
    Task = input("Choose Above and Enter the Letter:")
    print(Task)
    if Task.upper() == "A":
        Key = input("Enter Key: ")
        Value = input("Enter Value: ")

        Vault[Key] = Value
        print("Stored!")
    elif Task.upper() == "B":
        Deylet = input("What Key to Delete: ")
        del Vault[Deylet]
    elif Task.upper() == "C":
        print("THANKIESSS")
        break




#Anthony Joafil F. Crusante BSIT 1B
