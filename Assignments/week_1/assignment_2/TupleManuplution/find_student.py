
# 1. Take in the lower and upper roll number from the user. 
# 2. Then append the prefixes of the USN’s to the roll numbers. 
# 3. Using list comprehension, find out which USN’s lie in the given range. 
# 4. Print the list containing the tuples. 
# 5. Exit. 
# In the context of a university, a USN, or University Student Number, is a unique identifier 
# assigned to each student, acting as a primary identifier for their academic records and 
# interactions with the institution.

start=int(input("enter starting range"))
end=int(input("enter ending range"))
print(start)
print(end)

tup=(1,2,3,4,5,6,7,8,9)
print(tup[start:end])