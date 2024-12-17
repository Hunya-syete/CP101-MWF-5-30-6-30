import random

def guess_the_number():
    # Generate a random number between 1 and 20
    number_to_guess = random.randint(1, 20)
    max_attempts = 3

    print("Welcome to 'Guess the Number'!")
    print("I have picked a number between 1 and 20.")
    print(f"You have {max_attempts} attempts to guess it correctly.")

    for attempt in range(1, max_attempts + 1):
        try:
            # Prompt the user for a guess
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))

            if guess == number_to_guess:
                print("Congratulations! You guessed the correct number.")
                break
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input. Please enter an integer.")

    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

# Run the game
guess_the_number()
