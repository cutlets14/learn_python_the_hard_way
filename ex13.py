# Parameters, unpacking, and variables
from sys import argv

# script, first, second, third = argv

# print("This script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

# Combine argv and input()
script = argv

print("Welcome to this script:", script)
game = input("Would you like to play a game? Enter yes or no: ")
print(game.lower())
if game.lower() == "yes":
    print("Welcome to the funapolooza!")
else:
    print("Goodbye!")