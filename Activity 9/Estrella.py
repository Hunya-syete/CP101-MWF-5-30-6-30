def word_bank():
    words = [] 

    print("Welcome to the Word Bank program!")

    while True:
        word = input("Enter a word: ")
        words.append(word)  # Add the word to the list

        try_again = input("Do you want to try again? (Y/N): ").strip().lower()
        if try_again == 'n':
            break
        elif try_again != 'y':
            print("Invalid input. Please enter 'Y' or 'N'.")
    
   
    print(f"\nYou entered {len(words)} words.")
    print("Here are your words:")
    for word in words:
        print(f"- {word}")

word_bank()
