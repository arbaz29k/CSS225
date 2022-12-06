# Arbaz Khan
# 11/29/2022
# Problem 2 :- Writing a function that takes inputs from a user and prints whether the sum is greater than 10, less than 10, or equal to 10

def sum_10(): # Define function
  x = int(input("Enter a number: ")) # Ask user for input
  if x == 10: # Check if number equal to 10
    print("Number is equal to 10") # print to console
  elif x < 10: # Check if number less than 10
    print("Number is less than 10") # print to console
  elif x > 10: # Check if number greater than 10
    print("Number is greater than 10") # print to console
sum_10() #Call function & it will print automatically to console