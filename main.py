import random

# Functions
def number_check(question,low,high):
    error = "Please enter a whole number between 1 and 10"

    valid = False
    while not valid:
        try:
            response = int(input("How much would you like to play with? "))
            if 0 < response <= 10:
                print("You have asked to play with ${}".format(response))
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

def show_instructions ():
    print("*** How to Play the Lucky Unicorn game")
    print()
    print("The rules of the game are")
    print()



# Main routine
balance = 0
rounds_played = 0

print("Welcome to the Lucky Unicorn Game")

# ask user if played_before
played_before = yes_no("Have you played the game before? ")

# Ask user how much
how_much = number_check("How much would you like to play with?", 1, 10)
balance = how_much

# token generator


