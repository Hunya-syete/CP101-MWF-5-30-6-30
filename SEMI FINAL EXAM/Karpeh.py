def main():
    records = {}

    while True:
        print("\nChoose an option:")
        print("a. Add Data")
        print("b. Delete Data")
        print("c. End")

        choice = input("Enter your choice (a/b/c): ").strip().lower()

        if choice == 'a':
            key = input("Enter Key: ")
            value = input("Enter Value: ")
            records[key] = value
            print("Data added successfully.")
            print("Current Records:", records)

        elif choice == 'b':
            key = input("Enter Key to delete: ")
            if key in records:
                del records[key]
                print(f"Data with key '{key}' deleted successfully.")
            else:
                print(f"Key '{key}' not found.")
            print("Current Records:", records)

        elif choice == 'c':
            print("THANK YOU")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
