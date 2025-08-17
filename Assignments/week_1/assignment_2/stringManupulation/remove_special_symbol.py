# 5. Remove special symbols / punctuation from a string 
import string

input_string=input("please enter string with punctuation i will clean ")
clear_string=''
for x in input_string:
    if x not in string.punctuation:
        clear_string +=x
print(clear_string)