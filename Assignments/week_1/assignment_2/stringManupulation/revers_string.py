# 3. Reverse a given string 

# reversed a string using slicing with negative indexing

input_string=input("enter a string")
print(input_string)

#  text[::-1] tells Python:
# “Start from the end of the string, and go backwards one character at a time, until the beginning.”

revers=input_string[::-1]
print(revers)