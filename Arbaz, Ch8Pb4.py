# Arbaz Khan
# 11/29/2022
# Problem 3 :- Writing a function that takes a year as a parameter and returns True if the year is a leap year, False if it is otherwise
def leap_year(year): # Define function
  if (year % 4) == 0: # Check for divisibilty by 4
    if (year % 100) == 0: # Check for divisibilty by 100
      if (year % 400) == 0: # Check for divisibilty by 400
        print(f"{year} is a leap year") # print to console
      else:
        print(f"{year} is not a leap year") # print to console
    else:
        print(f"{year} is a leap year") # print to console
  else:
    print(f"{year} is not a leap year") # print to console
leap_year(2000)#Call function & it will print automatically to console