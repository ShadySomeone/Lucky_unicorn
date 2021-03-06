import random


# Functions
def number_check(question):
    error = "Please enter a whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            response = int(input(question))
            if 0 < response <= 10:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please enter yes or no")


def instructions():
    print("              *** How to Play the Lucky Unicorn game ***                ")
    print("                  *** The rules of the game are ***                     ")
    print("*** To play you must enter the amount of money you wish to play with ***")
    print("          *** This amount must be between 1 and 10 dollars ***          ")
    print("                      *** Each game costs $1 ***                        ")
    print("         *** Every game you are given 1 of 4 random tokens ***          ")
    print("        *** And each will give you a certain amount of money ***        ")
    print(" *** Unicorn gives $4, Horse and Zebra give $0.50 and Donkey give $0 ***")
    print("  *** You can quit at anytime but if you run out of money you lose ***  ")

# Main routine
balance = 0
rounds_played = 0

print("Welcome to the Lucky Unicorn Game")

# Ask user if played_before
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()
# Ask user how much
how_much = number_check("How much would you like to play with?")
balance = how_much
print("You have asked to play with ${}".format(how_much))


# Generate a Token
tokens = ["Unicorn", "Horse", "Zebra", "Donkey"]
selected_token = random.choice(tokens)
print(selected_token)
balance -= 1

# Ask user if they wish to play again
if selected_token == "Unicorn":
    balance += 4
    print("You got a Unicorn! You now have ${}".format(balance))
elif selected_token == "Horse":
    balance += 0.50
    print("You got a Horse! you now have ${}".format(balance))
elif selected_token == "Zebra":
    balance += 0.50
    print("You got a Zebra! You now have ${}".format(balance))
else:
    balance += 0
    print("Oh no, You got a Donkey! You now have ${}".format(balance))
