print("Welcome to my calculator by John Renz N. Rosagenia")
def mainloop():
    a = int(input("Enter your first number : "))
    b = int(input("Enter your first number : "))
    c = input('what you want to perform +,-,/,* : ')
    if c=='+':
        print("The sum is : " , a+b)
    if c=='-':
        print("The subtract is : " , a-b)
    if c=='*':
        print("The multiplication is : " , a*b)
    if c=='/':
        print("The division is : " , a/b)
    d = input("Do you want run again y/n : ")
    if d=='y':
        mainloop()
   
