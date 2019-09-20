# Zack Garzella
# Automatic Tipper
# The purpose is to calculate a 15% and 20% tip for a input dollar amount.

bill = input("Please enter the total bill ")
bill = int(bill)

# The following calucates the 15% and 20% tips

bill_15 = bill / 6.66666666666666666666666666666666666

bill_20 = bill / 5

print ("A 15% tip would be: ", bill_15)
print ("A 20% tip would be: ", bill_20)

input("\n\nPress the enter key to exit.")
