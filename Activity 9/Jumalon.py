def word_bank():
    words = []

    while True:
        word = input("Enter a word: ")
        words.append(word)


        try_again = input( "\nDo you want to try again? (Y/y for Yes, N/n for No): ").strip().lower()


        if try_again == 'n':
            break
        elif try_again != 'y':
            print("Invalid input! Please enter Y/y for Yes or N/n for No.")
    
  
    print(f"\nTotal number of words entered: {len(words)}")
    print("Words you entered:")
    for word in words:
        print(word)

word_bank()
    
    
