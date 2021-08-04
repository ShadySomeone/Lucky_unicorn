#Ask the user if they have played before
show_instruction = input("Have you played Lucky unicorn before?").lower().strip()
#If no display instructions if yes continue program
if show_instruction == "no":
    print("Print Instrutions")

elif show_instruction == "yes":
        print("Program continues")

elif show_instruction == "y":
        print("program continues")

elif show_instruction == "n":
        print("Print instructions")

else:
        print("Please enter Yes or No")
