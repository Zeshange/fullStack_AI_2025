#Calculate Compound Interest Use the formula:
#CI = P * (1 + R/100)**T - P
#Where P = principal, R = rate, T = time


P = float(input("Enter the principal amount (P): "))
R = float(input("Enter the annual interest rate (R) in %: "))
T = float(input("Enter the time duration (T) in years: "))

CI = P * (1 + R / 100) ** T - P
CI=round(CI,2)
print("Anual Intrest Amount is= ",CI)