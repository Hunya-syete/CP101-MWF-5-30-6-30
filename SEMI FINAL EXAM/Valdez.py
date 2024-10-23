# Rustom Carl M. Valdez BSIT 1styear CP101 (5:30-6:30pm)

def add_data(records):
    key = input("Enter Key(Lastname): ")
    value = input(f"Enter Value for Key {key}: ")
    records[key] = value 
    print(f"Added: {key} = {value}")

def delete_data(records):
    key = input("Enter Key to delete: ")
    if key in records:
        del records[key]
        print(f"Deleted: {key}")
    else:
        print(f"Key '{key}' not found.")

def display_records(records):
    print("Current Records:", records)

def main():
    records = {}

    while True:
        print("\nChoose an option:")
        print("a. Add Data")
        print("b. Remove Data")
        print("c. End")
        choice = input("Enter your choice (a b c): ").lower()
        if choice == 'a':
            add_data(records)
        elif choice == 'b':
            delete_data(records)
        elif choice == 'c':
            print("SALAMUCH! HAVE A NICE DAY!")
            break
        else:
            print("INVALID OPTION PLS TRY AGAIN")
        display_records(records)

main()
