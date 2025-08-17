#Distribute Items Equally - You have n candies and k students.
# Write a program to find:
# how many candies each student gets
# how many are left

candies=int(input("please enter candies  : "))
students=int(input("please enter students  : "))
candies_perHead=candies // students
print("Every student will receive ",candies_perHead ,"Candies")
remaining_Candies=candies % students
print("Remainging Candies are : ",remaining_Candies)
