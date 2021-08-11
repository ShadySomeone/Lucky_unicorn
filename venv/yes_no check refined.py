show_instruction = ""
while show_instruction.lower().strip() != "xxx":
    #Ask the user if they have played before
        show_instruction = input("Have you played the game before").lower()
    #If they say yes then continue the program
    #If they say no then display the instuctions
    #If they say anything else then Re ask the question
        if show_instruction == "yes" or show_instruction == "y":
            show_instruction = "yes"
            print("Program continues")
        elif show_instruction == "no" or show_instruction == "n":
            show_instruction = "no"
            print("Print instructions")
        else:
            print("Please enter yes or no")
            
