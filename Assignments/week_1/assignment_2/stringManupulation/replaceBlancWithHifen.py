# Python Program to Replace Every Blank Space with Hyphen in a String[The program takes a 
# string and replaces every blank space with a hyphen.

str=input("enter string with empty values")
# print(str)
newStr=""
for x in str:
    if x == " ":
       newStr += "-"
    else:
       newStr +=x
print(newStr)