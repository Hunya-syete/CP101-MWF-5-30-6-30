import random

def guess_the_number():
    # Generate a random number between 1 and 20
    number_to_guess = random.randint(1, 20)
    max_attempts = 3

    print("Welcome to 'Guess the Number'!")
    print("I have chosen a number between 1 and 20. You have 3 attempts to guess it.")

    for attempt in range(1, max_attempts + 1):
        # Get the user's guess
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check the guess
        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
            break
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")

        # Check if attempts are exhausted
        if attempt == max_attempts:
            print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}. Better luck next time!")

# Run the game
guess_the_number()
