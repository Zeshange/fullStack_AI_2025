import numpy as np
import pandas as pd

file_csv=pd.read_csv('Assignments\week2\RealEstate-USA (1).csv')
# print(file_csv)

# a=[1,2,4,5,6,7]
# sery=pd.Series(a)
# print(sery)

# data=[
#     {"name":"zeeshan","department":"web"},
#     {"name":"amina","department":"datascience"}
# ]

# df=pd.DataFrame(data)
# print(df)


df=pd.DataFrame(file_csv)
# print(df)
# print(df.info())
# print(df.dtypes)
# print(df.describe())
# print(df.shape)

# print(df.head(3))
# print(df.tail(9))
# print(df['city'])
# print(df['state'])
# print(df[['state','city']])

# print(df.loc[5])
# print(df.loc[[3,5,7]])
# print(df.loc[3:9])

# print(df.loc[df['price']> 100000])
# print(df.loc[df['city'] == 'Adjuntas'])

# print(df.loc[(df['city']=='Adjuntas') & (df['price'] < 180500)])

# print(df.loc[7,['city', 'price', 'street', 'zip_code', 'acre_lot']])

# print(df.loc[ : ,"city":"zip_code"])


# print(df.loc[df["city"]=="Adjuntas","city":"zip_code"])

# print(df.loc[df["city"].isin(["Adjuntas", "Ponce"])])
# print(df.loc[df["city"].isin(["Adjuntas", "Ponce"])].drop_duplicates(subset="city"))


# print(df.iloc[7])
# print(df.iloc[[3,5,7]])

# print(df.iloc[5:13])

# print(df.iloc[:,2])
# print(df.iloc[:,[2,4,6]])
# print(df.iloc[:,2:6])

# print(df.iloc[[2,4,7],[3,5]])
# print(df.iloc[[2,6],2:4])


# data = {
#     'city': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
#     'price': [150000, 10000, 110000, 11000, 120000, 125000, 130000],
#     'street': ['1st Ave', '2nd St', '3rd Blvd', '4th Dr', '5th Lane', '6th Way', '7th Cir'],
#     'zip_code': [601, 602, 603, 604, 605, 606, 607],
#     'acre_lot': [0.2, 0.25, 0.22, 0.3, 0.18, 0.35, 0.27]
# }

# df=pd.DataFrame(data)
# print(df)


# filtered_df = df.query("price < 120000 and city != 'B'")

# print(iltered_df)
# df_sorted = df.sort_values(by='price')
# print(df_sorted)


# new_row=pd.DataFrame([{"city":"nankana"}])

# df=pd.concat([df,new_row],ignore_index=True)
# print(df)

# df=df.drop(index=2)
# print(df)

# df=df.drop(index=range(4,6))
# print(df)

# df=df.drop(columns='price')
# print(df)

# df=df.drop(columns=['street','city'])
# print(df)
# df=df.dropna()
# df=df.fillna(0)
# print(df)
