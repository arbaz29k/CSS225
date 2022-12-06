# Arbaz Khan
# 11/29/2022
# Problem 1 :- Writing a function that takes two inputs from a user and prints whether they are equal or not

def check_equal(): # Define function
  a = int(input("Enter a number: ")) # Ask user for input
  b = int(input("Enter another number: ")) # Ask user for input
  if a == b: # Check if numbers are equal
    print("Numbers a and b are equal") # print to console
  elif a != b: # Check if numbers are not equal
    print("Numbers a and b are not equal") # print to console
check_equal()  # Call function & it will print automatically to console
