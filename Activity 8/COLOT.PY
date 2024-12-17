import random

def guess_the_number_game():
    secret_number = random.randint(1, 20)  # Generate a random number between 1 and 20
    attempts = 3  # Set maximum attempts

    print("Welcome to 'Guess the Number'!")
    print("I have chosen a number between 1 and 20. Can you guess it?")

    for i in range(attempts):
        guess = int(input(f"Attempt {i + 1}: Enter your guess: "))  # Prompt for user guess

        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break  # Exit the loop if guessed correctly
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    else:
        print(f"Sorry! The correct number was {secret_number}.")  # Reveal the number if not guessed

if __name__ == "__main__":
    guess_the_number_game()
