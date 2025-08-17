# 4. Take Input from user , and print prime number till that input number



num = int(input("Enter a number: "))

count = 1
while count <= num:
    if num % count != 0:
        print(count)
    count += 1
   
