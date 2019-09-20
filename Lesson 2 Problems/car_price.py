# Zack Garzella
# Car Salesman program
# The purpose ofthis program is to calculate the total price of a car...
# ...giving its base price.

print ("This will calculatethe total priceof your car")

base_price = input("Please enter the base price in whole dollars: ")
base_price = int(base_price)

# The following calculates the cost of all the fees

tax = base_price / 14.285714285714286

license_fee = base_price / 100

dealerPrepFee = 198

destCharge = 450

# This adds all the fees to the total price

total_price = base_price + tax + license_fee + dealerPrepFee + destCharge

print ("\nThe price of your car, including all fees, is $", total_price)

input("\n\nPress the enter key to exit.")
