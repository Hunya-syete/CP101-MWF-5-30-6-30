def word_bank():
    words = []

    while True:
        word = input("Enter a word: ")
        words.append(word)

        choice = input("Do you want to add another word? (Y/N): ")
        if choice == 'N' or choice == 'n':
            break

    print("\nYou entered", len(words), "words.")
    print("Here are the words:")
    for word in words:
        print(word)

# Run the word bank program
word_bank()
