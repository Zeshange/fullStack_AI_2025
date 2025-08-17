#Average of Three Numbers - Input three numbers and print their average.


num1=int(input("Please Enter Num 1:"))
num2=int(input("Please Enter Num 2:"))
num3=int(input("Please Enter Num 3:"))

average=(num1+num2+num3)/3
rounded_value=round(average,2)
print("Average of 3 givens numbers is = ",rounded_value)