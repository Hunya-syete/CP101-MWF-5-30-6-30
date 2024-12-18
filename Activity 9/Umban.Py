def word_bank():
    words = []

    while True:
        word = input("Enter a word: ")
        words.append(word)

        try_again = input("Do you want to enter another word? (Y/N): ").strip().lower()
        if try_again != 'y':
            break

    # Display total number of words and the list of words
    print(f"\nTotal number of words: {len(words)}")
    print("Words entered:")
    for word in words:
        print(word)

# Start the word bank program
word_bank()
