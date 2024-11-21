def word_bank():
    words = []

    while True:
        word = input("Enter a word: ")
        words.append(word)
        
        try_again = input("Do you want to enter another word? (Y/y for Yes, N/n for No): ").strip().lower()
        
        if try_again == 'n':
            print(f"\nYou entered {len(words)} words.")
            print("Here are all the words you entered:")
            for w in words:
                print(w)
            break
        elif try_again != 'y':
            print("Invalid input. Please enter 'Y' to continue or 'N' to stop.")

word_bank()
