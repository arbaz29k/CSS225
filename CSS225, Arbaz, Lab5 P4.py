# Arbaz
# 11/05/2022
# This program will iterate the integers from 1 to 50. For multiples of three print “Divisible by three”
# This program will  multiples of five print “Divisible by five”.
# For numbers which are multiples of both three and five print “Divisible by both”.
# If none is applicable than print "Divisible by none."

for i in range(51):
    if(i%3==0 and i%5==0):
        print(i," is Divisible by both three and five.")
    elif(i%5==0):
        print(i," is Divisible by five.")
    elif(i%3==0):
        print(i," is Divisble by three.")
    else:
        print(i," is Divisble by none.")