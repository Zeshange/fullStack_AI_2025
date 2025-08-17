# [The program takes three sides of a triangle and 
# prints the area formed by all three sides.]
import math

sideOne=int(input("Enter side one"))
sideTwo=int(input("Enter side one"))
sideThree=int(input("Enter side one"))

s=(sideOne+sideTwo+sideThree)/2

area=math.sqrt(s*(s-sideOne)*(s-sideTwo)*(s-sideThree))
print(round(area,2))