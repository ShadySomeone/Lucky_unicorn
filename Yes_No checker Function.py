#Functions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            print("Program continues")
        elif response == "no" or response == "n":
            print("Print instructions")
        else:
            print("Please enter yes or no")

show_instructions = yes_no("Have you played the game before? ")
