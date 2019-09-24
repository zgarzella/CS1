# Zack Garzella
# Rock, Paper, Scissors
# This program tells the user to input rock, paper, or scissors, then randomly...
# generates a different answer and tells the user if they won

import random

replay = "yes"

while replay == "yes":
    user_input = input("Please enter 'rock', 'paper' or 'scissors': ")



# This converts the user's input into lowercase which will prevent errors

    user_input = user_input.lower()

# This converts the user's choice to a number, which makes it easier to print...
# ...in the if and elif statements later

    if user_input == "rock" :
        user_input = 1

    elif user_input == "paper" :
        user_input = 2

    elif user_input == "scissors" :
        user_input = 3

# This generates a random answer from the cpu with "1" representing rock, "2"...
# ...representing paper, and "3" representing scissors

    cpu_input = random.randint(1,3)

# This takes the user's input and the cpu's input to generate and print an...
# ...answer for the user


    if user_input == 1 and cpu_input == 1:
        print ("You tied, both you and the cpu chose rock")

    elif user_input == 2 and cpu_input == 2:
        print ("You tied, both you and the cpu chose paper")

    elif user_input == 3 and cpu_input == 3:
        print ("You tied, both you and the cpu chose scissors")

    elif user_input == 1 and cpu_input == 2:
        print ("You lost, you chose rock and the cpu chose paper")

    elif user_input == 2 and cpu_input == 3:
        print ("You lost, you chose paper and the cpu chose scissors")

    elif user_input == 3 and cpu_input == 1:
        print ("You lost, you chose scissors and the cpu chose rock")

    elif user_input == 3 and cpu_input == 2:
        print ("You won, you chose scissors and the cpu chose paper")

    elif user_input == 2 and cpu_input == 1:
        print ("You won, you chose paper and the cpu chose rock")

    elif user_input == 1 and cpu_input == 3:
        print ("You won, you chose rock and the cpu chose scissors")

# This else statement outputs an error message if the user inputs an answer...
#... incorrently

    else:
        print("Error, please enter a valid input")

    replay = input("\nDo you want to play again? Enter yes or no: ")

input("\n\nPress enter key to exit")
