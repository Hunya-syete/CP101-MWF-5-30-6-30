import random

def guess_the_number():
    # Generate a random number between 1 and 20
    number_to_guess = random.randint(1, 20)
    attempts = 3

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 20.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the number!")
            break
    else:
        print(f"Sorry! The number was {number_to_guess}. Better luck next time!")

# Start the game
guess_the_number()
