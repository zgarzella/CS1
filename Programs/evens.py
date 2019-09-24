# Zack Garzella
# This program asks the user for a int between 0 and 10, then outputs...
# ... all the even numbers between the number and 0

number = int(input("Enter a whole number between 0 and 20: "))



if number < 0 or number > 20:
          print("ERROR, Please enter a valid number")

count = 0
while count <= number :
          print(count, end = " ")
          count += 2

input("\n\nPress enter key to exit ")
