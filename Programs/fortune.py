# Zack Garzella
# Fortune Cookie
# This program will display a random fortune to the user

import random

name = input("Enter your name: ")

fortune_1 = str("you will recieve something today")
fortune_2 = str("you will need to do something today")
fortune_3 = str("you will find something today")
fortune_4 = str("you will want to see someone today")
fortune_5 = str("you will need someone today")
fortune_6 = str("you will have a good day")
fortune_7 = str("you will have a bad day")
fortune_8 = str("you will have a good life")

# This variable randomly generates a number

user_fortune = random.randint(1,8)

# These if/elif statements print the fortune based on the randomly generated...
#... number

if user_fortune == 1:
    print(name ,fortune_1)

elif user_fortune == 2:
    print(name ,fortune_2)

elif user_fortune == 3:
    print(name ,fortune_3)

elif user_fortune == 4:
    print(name ,fortune_4)

elif user_fortune == 5:
    print(name ,fortune_5)

elif user_fortune == 6:
    print(name ,fortune_6)

elif user_fortune == 7:
    print(name ,fortune_7)

elif user_fortune == 8:
    print(name ,fortune_8)

# This else statement will show if there is something wrong with the randomly...
#... generated number

else:
    print ("Error invalid fortune")

input("\n\nPress enter key to exit")
