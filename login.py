Name = Arbaz
date = 10/11/2022
# week one lab
# purpose: This program grants you access if your user is "jack" and "Jill" if not the access will denied

#!/usr/bin/env python
username = input("Login: >> ")
user1 = "Jack"
user2 = "Jill"
if username == user1:
    print("Access granted")
elif username == user2:
    print("Welcome to the system")
else:
    print("Access denied")
