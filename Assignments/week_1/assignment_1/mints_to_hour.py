# Convert Minutes to Hours and Minutes 
# Input number of minutes and convert to hours and remaining minutes. 
# Example: 130 minutes → 2 hours 10 minutes 


minuts=int(input("please enter numbers of minuts i will convert it to hours :"))
hours=minuts //60
mints=minuts % 60
print("hours :",hours)
print("minuts :",mints)