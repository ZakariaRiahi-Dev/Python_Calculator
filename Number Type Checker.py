user_input = str(input("Enter a string: "))

pair_characters = user_input[::2]

print("Characters at pair positions are: " + pair_characters)

user2_input = str(input("Enter a string: "))

impair_characters = user2_input[1::2]

print("Characters at impair positions are: " + impair_characters)