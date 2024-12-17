# Initialize an empty dictionary to store data
record_dict = {}

# Function to display the current record
def display_record():
    print("Current Records:", record_dict)

# Main loop for the application
while True:
    # Prompt the user for an action
    action = input("Choose an action (Add Data, Delete Data, End): ").strip().lower()

    if action == "add data":
        # Add data
        key = input("Enter key: ").strip()
        value = input("Enter value: ").strip()
        record_dict[key] = value
        print(f"Added {key}: {value}")
        display_record()

    elif action == "delete data":
        # Delete data
        key = input("Enter key to delete: ").strip()
        if key in record_dict:
            del record_dict[key]
            print(f"Deleted key: {key}")
        else:
            print(f"Key '{key}' not found.")
        display_record()

    elif action == "end":
        # End the program
        print("THANK YOU")
        break

    else:
        print("Invalid action. Please choose 'Add Data', 'Delete Data', or 'End'.")
