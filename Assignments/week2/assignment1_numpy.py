# 1:A Simple Task for NUMPY:
# Dataset under discussion - Sample URL:
# https://github.com/ShahzadSarwar10/FULLSTACK-WITH-AI-BOOTCAMP-B1-MonToFri-2.5MonthExplorer/blob/main/DataSetForPractice/RealEstate-USA.csv
# It is REAL ESTATE – US data.
# TASK:
# 1. Load above CVS file above, into separate – Array , with NUMPY, following columns
# “brokered_by”, 
# “price”
# “acre_lot”
# “city”
# “house_size”

import numpy as np

broked_by,price,acre_lot,city,house_size=np.genfromtxt('Assignments\week2\RealEstate-USA (1).csv', delimiter=',', usecols=(0,2,4,5,10), unpack=True, dtype=None,skip_header=(1))

# print("broked_by",broked_by)
# print("price",price)
# print("acre_lot",acre_lot)
# print("city",city)
# print("house_size",house_size)



# # Adding array of price and home_size

# print(price + house_size)

# #Subtracting array of price and home_size

# print(price - house_size)

# #Multiplication array of price and home_size

# print(price * house_size)




#. Create a “2D array” based on array of [array of “price”] and [array of “house_size”]
# Print it.


# d2=np.array([[1,2],[3,4]])
# print(np.ndim(d2))
# print(d2.dtype)
# print(type(d2))
#. Create a “3D array” based on array of [array of “price”] and [array of “house_size”]
# Print it.



# d3 = np.array([[[1,5],[3,4]],[[4,5],[5,6]]])
# # print(d3)
# print(np.ndim(d3))
# print(np.size(d3))



# print(price)

# print(np.shape(price))
# print(np.size(price))
# print(np.ndim(price))
# print(type(price))
# print(price.dtype)
# print(len(price))
# print(np.mean(price))
# print(np.min(price))
# print(np.max(price))
# print(np.cumprod(price))
# print(np.cumsum(price))


# 10. Slice array of [Question 5, as - “2D array” based on array of [array of “price”] and [array of 
# “house_size”] ]
# Row : from 1st
#  value to 3rd value
# Column: from 2nd value to 4th value

# arr=np.array([price,house_size])


# print(arr[0:2,2:5])


# arr=np.array([price,house_size])
# sinethita=np.sign(arr)
# costhita=np.cos(arr)
# tan=np.tan(arr)

# invers_sinethita=np.arcsin(arr)
# invers_costhita=np.arccos(arr)
# invers_tan=np.arctan(arr)

