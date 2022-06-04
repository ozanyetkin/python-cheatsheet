capitals = ["Stockholm", "Budapest", "Helsinki","Copenhagen", "Oslo", "Paris"]

try:
    city = capitals[8]
    # capitals.remove("Seattle")
    capitals.remove("Stockholm")
    capitals.remove("Washington")
except ValueError:
    capitals = capitals
except IndexError:
    print("index error occurred")

try:
    y = 10 / 0
except ZeroDivisionError:
    print("zero division is not possible")
    
"""
Write a program that asks the user to enter two values 
and gives the sum of two values as the output. 
If the user input two different data types, give an error message.
"""

# Calculate the mean of the list below:
# nums = [65, 27, "-", 48, 95, "-", 78, 96, 100]

"""
Assuming that we have some email addresses
in the "username@companyname.com"
format, please write program to print the user
name of a given email address. Both user
names and company names are composed of
letters only
"""