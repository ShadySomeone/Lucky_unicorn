import random

#Functions go here

tokens = ["Unicorn", "Horse", "Zebra", "Donkey" ]

#Main routine goes here
selected_token = random.choice(tokens)
print(selected_token)
balance = 0

tokens = ["Unicorn", "Horse", "Zebra", "Donkey" ]


if selected_token == "Unicorn":
    balance += 4
elif selected_token == "Horse":
    balance += 0.5
elif selected_token == "Zebra":
    balance += 0.5
else:
    balance += 0

print(balance)
