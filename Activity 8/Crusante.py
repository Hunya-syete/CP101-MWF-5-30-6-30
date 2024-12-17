# Online Python compiler (interpreter) to run Pythoimport random

def Guesser():
  print("Random Number Guessing")
  print("Guess the Correct Number Between 1 and 20")
  print("You only have 3 Attempts")
  
  Lo = 1
  Hi = 20
  Attempts = 0
  Max_Attempts = 3
  
  RN = random.randint(Lo, Hi)
  
  while Attempts < Max_Attempts:
    GN = int(input("What's the number?: "))
    Attempts += 1
    
    if GN > RN:
      print("lower")
          
    elif GN < RN:
      print("Higher")
      
    elif GN == RN:
      print("Correct")
      break
  
    if Attempts == Max_Attempts:
        print("Maximum Attempts Reached!")
        print("Try Again!")
        break
 
Guesser()




# Anthony Joafil F. Crusante (BSIT 1-B)
