def word_bank():
    words = []  # List to store words

    print("Welcome to the Word Bank program!")
    
    while True:
        # Ask user to enter a word
        word = input("Enter a word: ")
        words.append(word)  # Add word to the list
        
        # Ask if the user wants to try again
        try_again = input("Do you want to add another word? (Y/y for Yes, N/n for No): ").strip().lower()
        
        if try_again == 'n':  # Exit the loop if the user says 'No'
            break
        elif try_again != 'y':  # Handle invalid input
            print("Invalid choice. Please enter 'Y' or 'N'.")
    
    # Display the results
    print("\nWord Bank Summary:")
    print(f"Total number of words: {len(words)}")
    print("Words entered:")
    for word in words:
        print(f"- {word}")

# Run the program
word_bank()
