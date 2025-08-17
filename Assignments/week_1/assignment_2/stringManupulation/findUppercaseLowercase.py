# Python Program to Count Number of Uppercase and Lowercase Letters in a String[The program 
# takes a string and counts the number of lowercase letters and uppercase letters in the string.]


str=input("enter a string without space")
uper=0
lower=0
for char in str:
    if char.isupper():
        uper += 1
    elif char.islower():  
        lower += 1
    

print(uper)
print(lower)