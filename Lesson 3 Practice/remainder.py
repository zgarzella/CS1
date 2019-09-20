# Zack Garzella
# Remainder Program
# This program divids two integers and finds the remainder

large_num = input("Enter a large integer: ")
large_num = int(large_num)

small_num = input("Enter a small integer: ")
small_num = int(small_num)

quotient = (large_num / small_num)
quotient = int(quotient)

remainder = (large_num % small_num)
remainder = int(remainder)

large_num_str = str(large_num)
small_num_str = str(small_num)
quotient_str = str(quotient)
remainder_str = str(remainder)
                    
print(large_num_str, "divided by", small_num_str, ("is"), quotient_str + ("r."),
      remainder_str)

input = ("\n\n Press enter key to exit") 
