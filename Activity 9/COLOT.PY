# Simple Word Bank Program

words = []  # Initialize an empty list to store words

while True:
    word = input("Enter a word: ")  # Ask the user to enter a word
    words.append(word)  # Store the word in the list

    # Ask if the user wants to try again
    again = input("Do you want to enter another word? (Y/N): ").strip().lower()
    if again == 'n':  # If user chooses No
        break  # Exit the loop

# Display the total number of words and the words entered
print("\nTotal number of words:", len(words))
print("Words entered:")
print(", ".join(words))  # Print all words separated by commas
