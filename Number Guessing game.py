import random


RandomNumber = random.randint(1, 10)
try:
    Userinput = int(input("Enter a number between 1 and 10: "))
except:
    print("Please enter a number")

while True:
    if Userinput == RandomNumber:
        print("You have guessed the correct number")
        break
    else:
        print("Try again")
        Userinput = int(input("Enter a number between 1 and 10: "))