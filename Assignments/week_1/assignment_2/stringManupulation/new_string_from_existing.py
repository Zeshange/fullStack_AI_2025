# 1. Write a program to create a new string made of an input string’s first, 
# middle, and last character. 

input_value=input("please enter a string :")
print(input_value)

first_chr=input_value[0]
last_chr=input_value[-1]
middle_char=input_value[len(input_value)//2]
new_string=first_chr + last_chr + middle_char
print(new_string)