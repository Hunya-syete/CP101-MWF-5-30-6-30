import random

def guess_the_number():
 
  secret_number = random.randint(1, 20)
  
  max_attempts = 3
  attempts = 0
  
  print("Welcome to the Guess the Number game!")
  print("I've chosen a number between 1 and 20.")
 
  while attempts < max_attempts:
    try:
     
      guess = int(input(f"Take a guess ({attempts+1}/{max_attempts}): "))
      
 
      if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempts+1} attempts!")
        return
      
     
      elif guess < secret_number:
        print("Too low! Try again.")
      else:
        print("Too high! Try again.")
      
    
      attempts += 1
    except ValueError:
      print("Invalid input. Please enter a number.")
  
  print(f"You ran out of attempts! The number was {secret_number}")


guess_the_number()
