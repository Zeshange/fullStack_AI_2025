# Python Program to Find the Larger String without using Built-in Functions[The program takes in 
# two strings and display the larger string without using built-in function.

str1=input("Enter string one")
str2=input("Enter string Two")
count1=0
count2=0
for x in str1:
    count1 +=1

for x in str1:
    count2 +=1

if count1 > count2:
    print("string 1 is grater :",str1)
else:
    print("string 2 is grater :",str2)
