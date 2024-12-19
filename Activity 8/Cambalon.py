def Guesser():
  print("Random Number Guessing")
  print("Guess the Correct Number Between 1 and 20")
  print("You only have 3 Attempts")
  
  Low = 1
  High = 20
  Attempts = 0
  Max_Attempts = 3
  
  RN = random.randint(Low, High)
  
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
