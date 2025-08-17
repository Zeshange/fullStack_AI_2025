# 2. Take Input from user , and print even number till that input number

num=int(input("Enter a number i will print even number till that number"))
count=0
while count <= num:
    if count % 2==0:
        print(count)
    count +=1