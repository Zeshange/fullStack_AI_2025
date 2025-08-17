# Salary Calculator 
# Input basic salary. Calculate: 
#  HRA = 20% of basic 
#  DA = 15% of basic 
#  Total Salary = Basic + HRA + DA

basic_salary=int(input("please enter basic salary"))
HRA=(basic_salary * 20)/100
DA=(basic_salary*15)/100
print(HRA,DA)
total_salary=basic_salary + HRA + DA
print("Your total salary is :",total_salary)