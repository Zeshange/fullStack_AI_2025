#  Python Program to Check if the Substring is Present in the Given String. [The program takes a 
# string and checks if a substring is present in the given string.

mainString=input("enter string") 
substring=input("enter another string")
if substring in mainString:
    print('substring exist in mainstring')
else:
    print("substring is not exist")