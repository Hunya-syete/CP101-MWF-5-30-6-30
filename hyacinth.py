import random

def guess_the_number():
    
    secret_number = random.randint(1, 20)
    attempts = 3 
    
    print("I'm thinking of a number between 1 and 20. You have 3 attempts to guess it!")

    
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Take a guess: "))

      
        if guess == secret_number:
            print("Congratulations! You guessed the number correctly!")
            return  
        elif guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

    
    print(f"Sorry, you've used all {attempts} attempts. The number was {secret_number}.")

guess_the_number()
