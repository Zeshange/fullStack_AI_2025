import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/haseebtariq/Documents/GitHub/full-stack-ai./week3/RealEstate-USA.csv', delimiter =",")

# Display the DataFrame
print(df)

df.info() 
df.dtypes 
df.describe() 
df.shape 


print(df.to_string(max_rows=201))
print(df.head(7))
print(df.tail(9))

df.to_string(column=["city"])
print("city")

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(df['city'])
print(df['street'])
df[['city', 'street', 'state']]
print(df[['city', 'price', 'street']])


print(df.loc[5])
print(df.loc[[3,5,7]])
print(df.loc[3:9])
print(df.loc[df['price']>100000])
print(df.loc[df['city'] =='Adjuntas'])
print(df.loc[df['city'] =='Adjuntas'])
print(df.loc[df['price'] <=180500])

print(df.loc[7,['city', 'price' , 'street' , 'zip_code' , 'acre_lot' ]])
s = (df.loc[:, 'city':'zip_code'])
print(s)
print(df['zip_code'])


df1 = (df.loc[df['city'] =='Adjuntas'])
df2 = (df.loc[:, 'city':'zip_code'])
df_combined = pd.concat([df1 , df2])
print(df_combined)

print(df.iloc[5])
print(df.iloc[[7,9,15]])
print(df.iloc[5:13])
print(df.iloc[:,3])
print(df.iloc[:,[2,4,9]])
print(df.iloc[:,2:5])

cd1 = (df.iloc[[7,9,15]])
cd2 = (df.iloc[:,[2,4]])
df_combined = pd.concat([cd1 , cd2])
print(df_combined)

cd3 = df.iloc[2:6, 2:6]
print(cd3)

df.loc[len(df.index)] = [1589,'for_sale',239000,7,3,0.31,155166,'Arecibo','Puerto Rico11',612,2715,'']
print(df.tail)

inplace=True


df_new = df.drop(2)

print(df_new)

df_new2 = df.drop([4,5,6,7,])

print(df_new2)

print(df.drop('house_size', axis=1))

print(df.rename(columns={'state': 'state_Changed'}))

print(df.rename(index={3: 5}))

print(df)

print(df.query('price < 127400 and city != "Adjuntas"'))

print(df.sort_values('price'))

print(df.groupby('city')['price'].sum())

print(df.dropna())
print(df)

df_new3 = df.fillna(0)
print(df_new3)