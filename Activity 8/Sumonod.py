import random
# Generate a random number between 1 and 100
secret_number = random.randint(1, 20)
# Start the game
print("Welcome to 'Guess the Number' game!")
print("I'm thinking of a number between 1 and 20.")
# Variable to store the user's guess
guess = None

# Variable to count the number of attempts
attempts = 0
# Loop until the user guesses the correct number
while guess != secret_number:
    # Ask the user to enter a number
    guess = int(input("Enter your guess: "))

    # Increment the attempts counter
    attempts += 1

    # Check if the guess is too low, too high, or correct
    if guess < secret_number:
        print("Too low! Try guessing a higher number.")
    elif guess > secret_number:
        print("Too high! Try guessing a lower number.")
    else:
        print("Congratulations! You guessed the correct number!")
        # Tell the user how many attempts it took
print(f"It took you {attempts} attempts to guess the correct number.")
print("Thank you for playing!")

        
        
        
        
