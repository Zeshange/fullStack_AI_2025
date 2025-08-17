import numpy as np


# loading data

brokered_by, status, price, acre_lot, city, house_size = np.genfromtxt("C:\\Users\\Hp\\Documents\\GitHub\\full-stack-ai\\week3\\RealEstate-USA.csv", delimiter=',', usecols=(0, 1, 2, 3, 7,10), unpack=True, skip_header=1)


print(brokered_by)
print(status)
print(price)
print(acre_lot)
print(city)
print(house_size)

# operation on array of "price"

print("RealEstate-USA Price mean: " , np.mean(price))
print("RealEstate-USA Price average: " , np.average(price))
print("RealEstate-USA price std: " , np.std(price))
print("RealEstate-USA Price mod: " , np.median(price))
print("RealEstate-USA Price percentile -35: " , np.percentile(price,35))
print("RealEstate-USA Price percentile  -65: " , np.percentile(price,65))

# operation on array of “house_size”

print("RealEstate-USA Price mean: " , np.mean(house_size))
print("RealEstate-USA Price average: " , np.average(house_size))
print("RealEstate-USA price std: " , np.std(house_size))
print("RealEstate-USA Price mod: " , np.median(house_size))
print("RealEstate-USA Price percentile -35: " , np.percentile(house_size,35))
print("RealEstate-USA Price percentile  -65: " , np.percentile(house_size,65))


# arithmetic operations ON house_size , price

addition = price + house_size
subtraction = price - house_size
multiplication = price * house_size

print(addition)
print(subtraction)
print(multiplication)

#handeling nan

np.nan_to_num(price)
np.nan_to_num(house_size)

# creating 2d array

stack2d = np.array([price, house_size]).T
print(stack2d)

# creating 3d array

stack3d = np.array([price, house_size, acre_lot]).T
print(stack3d)

# Iterate the array

for x in  np.nditer(price):
        print(x)

# Iterate the array

for y in np.ndenumerate(price):
        print(y)      

# common prpoerties

print(price.ndim)
print(price.shape)
print(price.size)
print(price.itemsize)
print(price.nbytes)
print(price.dtype)
print(price.flags)      

#Q10 slicing array

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