#!/usr/bin/env python3
import getpass
def test(user,password):
    return True if user == password else False

user = getpass.getuser()
password = getpass.getpass()

if test(user,password):
    print("yeah!")
else:
    print("denied!")






