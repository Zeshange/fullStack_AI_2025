#  Python Program to Create a List of Tuples with the First Element as the Number and Second 
# Element as the Square of the Number. The program takes a range and creates a list of tuples 
# within that range with the first element as the number and the second element as the square of 
# the number.  


start=int(input("type start range"))
end=int(input("type end range"))

print(start)
print(end)

result=[]

for x in range(start ,end+1):
    result.append((x,x**2))

print(result)


