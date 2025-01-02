String = input("Enter a string: ")

String = String.lower()
while True:
    if String == String[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")
        continue_game = input("Do you want to play again? (yes/no): ")
        if continue_game == "yes":
            continue
        else:
            break

