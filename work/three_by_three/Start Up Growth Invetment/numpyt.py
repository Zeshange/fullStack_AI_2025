import numpy as np

#loading data
Startup_Name ,industry,Funding_Rounds, Valuation_USD, Number_of_Investors,Country,Year_Founded = np.genfromtxt("C:\\Users\\Hp\\Documents\\GitHub\\Full-Stack-Ai\\Start Up Growth Invetment\\startup_growth_investment_data.csv", delimiter=',', usecols=(0,1,2,3,5,6,7),unpack=True, skip_header=1)

# replace nan values with 0
Startup_Name ,industry,Funding_Rounds, Number_of_Investors,Country,Year_Founded = np.nan_to_num(Startup_Name, nan=0), np.nan_to_num(industry, nan=0), np.nan_to_num(Funding_Rounds, nan=0), np.nan_to_num(Number_of_Investors, nan=0), np.nan_to_num(Country, nan=0), np.nan_to_num(Year_Founded, nan=0)



#printing the loaded data
print(Startup_Name)
print(industry)
print(Funding_Rounds)
print(Valuation_USD)
print(Number_of_Investors)
print(Country)
print(Year_Founded)


# operation on array of Funding_Rounds

print("startup_growth_investment_data.csv Funding_Rounds mean: " , np.mean(Funding_Rounds))
print("startup_growth_investment_data.csv Funding_Rounds average: " , np.average(Funding_Rounds))
print("startup_growth_investment_data.csv Funding_Rounds std: " , np.std(Funding_Rounds))
print("startup_growth_investment_data.csv Funding_Rounds mod: " , np.median(Funding_Rounds))
print("startup_growth_investment_data.csv Funding_Rounds -35: " , np.percentile(Funding_Rounds,35))
print("startup_growth_investment_data.csv Funding_Rounds percentile  -65: " , np.percentile(Funding_Rounds,65))


# operation on array of Valuation (USD)

print("startup_growth_investment_data.csv Valuation (USD) mean: " , np.mean(Valuation_USD))
print("startup_growth_investment_data.csv Valuation (USD) average: " , np.average(Valuation_USD))
print("startup_growth_investment_data.csv Valuation (USD) std: " , np.std(Valuation_USD))
print("startup_growth_investment_data.csv Valuation (USD) mod: " , np.median(Valuation_USD))
print("startup_growth_investment_data.csv Valuation (USD) -35: " , np.percentile(Valuation_USD,35))
print("startup_growth_investment_data.csv Valuation (USD) percentile  -65: " , np.percentile(Valuation_USD,65))

# arithmetic operations on Funding_Rounds and Valuation_USD

addition = Funding_Rounds + Valuation_USD
subtraction = Funding_Rounds - Valuation_USD
multiplication = Funding_Rounds * Valuation_USD

print(addition)
print(subtraction)
print(multiplication)


# creating 2d array

stack2d = np.array([Funding_Rounds, Valuation_USD]).T
print(stack2d)

# creating 3d array

stack3d = np.array([Funding_Rounds, Valuation_USD, Number_of_Investors]).T
print(stack3d)

# Iterate the array

for x in  np.nditer(Valuation_USD):
        print(x)

# Iterate the array

for y in np.ndenumerate(Valuation_USD):
        print(y)    


# Printing common prpoerties

print(Valuation_USD.ndim)
print(Valuation_USD.shape)
print(Valuation_USD.size)
print(Valuation_USD.itemsize)
print(Valuation_USD.nbytes)
print(Valuation_USD.dtype)
print(Valuation_USD.flags)      

# slicing array

print(stack2d[0:3 , 1:2])

# slicing array

print(stack2d[2:8 ,3:5])

# geometric operation in NUMPY

stack2d = np.nan_to_num(stack2d) 
print(np.sin(stack2d))
print(np.cos(stack2d))
print(np.tan(stack2d))
print(np.arcsin(stack2d))
print(np.arccos(stack2d))
print(np.arctan(stack2d))
