#!/usr/bin/python3
# Author: Danny Whitaker
# Date: 2/4/25
# Version 1.1

"""
This program is a program designed to ask what is your name, and then respond with "Hello"
"""

# Create an input from the user to which the system can respond to
username = input("What is your username? ")
text = "Hello, "
print(text,username)
number = int(input("What number do you want me to repeat? "))
print("Number", number)
numbers = int(input("What number do you want to add with 6 that comes out below 10? "))
result = numbers + 6

if result >= 10 or result == 10:
    print("That number is greater than or equal to 10")
else:
    print(f"{numbers} + 6 = {result}")
