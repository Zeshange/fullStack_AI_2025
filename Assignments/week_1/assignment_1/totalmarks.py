# Total Marks and Percentage
# Input marks of 5 subjects. Print:
#  Total marks
#  Percentage
#  Average
  
# urdu, english, math, computer, islamiyat = map(int, input("Please enter marks of 5 subjects separated by space: ").split())
 
i=0
list=["urdu","english","math","computer","physics"]
while i<5 :
    list[i]=int(input(f"please enter marks {list[i]} :"))
    i=i+1
    
print(list)
total=0
for x in list:
    total +=x
average=total/5
persent=(total*100)/500
print(f"your total marks is : {total} out of 500")
print(f"your average marks is {average}")
print(f"your Percentage  is {persent}")


