def word_bank():
    words = []

    while True:
        # Ask user to enter a word
        word = input("Enter a word: ").strip()
        words.append(word)

        # Ask if the user wants to try again
        try_again = input("Do you want to add another word? (Y/N): ").strip().lower()
        if try_again not in ('y', 'yes'):
            break

    # Display the total number of words and the words entered
    print(f"\nYou entered {len(words)} words.")
    print("Words:")
    for word in words:
        print(f"- {word}")

# Run the word bank program
word_bank()
