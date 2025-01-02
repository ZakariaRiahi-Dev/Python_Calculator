print("Welcome to the calculator program")

First_num = float(input("Enter the first number: "))

Second_num = float(input("Enter the second number: "))

Operation = input("Enter the operation you want to perform + or - or / or *: ")

if Operation == "+":
    print("The result is: ", float(First_num) + float(Second_num))
elif Operation == "-":
    print("The result is: ", float(First_num) - float(Second_num))
elif Operation == "/":
    print("The result is: ", float(First_num) / float(Second_num))
elif Operation == "*":
    print("The result is: ", float(First_num) * float(Second_num))
else:
    print("Invalid operation")

print("Thank you for using the calculator program")
exit()
