# Zack Garzella
# Coin Flip
# This program simulates flipping a coin 10 times

import random

# This represtents a coin flipping with 1 being heads and 2 being tails 

heads_tails = random.randint(1,2)

heads = 0

tails = 0

if heads_tails == 1:
    heads += 1

if heads_tails == 2:
    tails += 1

# This repeats the coin flipping 9 more times and could be improved with a function

heads_tails = random.randint(1,2)

if heads_tails == 1:
    heads += 1

if heads_tails == 2:
    tails += 1

heads_tails = random.randint(1,2)

if heads_tails == 1:
    heads += 1

if heads_tails == 2:
    tails += 1

heads_tails = random.randint(1,2)

if heads_tails == 1:
    heads += 1

if heads_tails == 2:
    tails += 1

heads_tails = random.randint(1,2)

if heads_tails == 1:
    heads += 1

if heads_tails == 2:
    tails += 1

heads_tails = random.randint(1,2)

if heads_tails == 1:
    heads += 1

if heads_tails == 2:
    tails += 1

heads_tails = random.randint(1,2)

if heads_tails == 1:
    heads += 1

if heads_tails == 2:
    tails += 1

heads_tails = random.randint(1,2)

if heads_tails == 1:
    heads += 1

if heads_tails == 2:
    tails += 1

heads_tails = random.randint(1,2)

if heads_tails == 1:
    heads += 1

if heads_tails == 2:
    tails += 1

heads_tails = random.randint(1,2)

if heads_tails == 1:
    heads += 1

if heads_tails == 2:
    tails += 1

print("It was heads", heads,"times")
print("It was tails", tails,"times")

input("\n\nPress enter key to exit")
