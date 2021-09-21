#Functions go here
def show_instructions ():
    print("*** How to Play the Lucky Unicorn game")
    print()
    print("The rules of the game are")
    print()

def yes_no(question):
    error =("Please answer yes or no")

    response = input(question)

    if response == "no":
        return response
    elif response =="yes":
        return response
    else:
        print(error)


#Main routine goes here
played_before = yes_no("Have you played Lucky Unicorn before?")

if played_before == "no":
    print(show_instructions)


