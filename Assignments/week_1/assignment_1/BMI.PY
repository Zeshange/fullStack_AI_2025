# Calculate Body Mass Index (BMI) 
# Input weight (kg) and height (m), then calculate: 
# BMI = weight / (height ** 2)
weight=float(input("enter wight in kg"))
height=float(input("height in feet"))
meter=height * 0.3048
bmi=weight / (meter **2)
rounded_bmi=round(bmi,2)
print("your body mass indes is: ",rounded_bmi)