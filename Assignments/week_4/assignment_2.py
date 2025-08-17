# Task 2- Linear Regression SK Learn implementation: 
# A Simple Task for Linear Regression SK Learn implementation : 
# Dataset under discussion - Sample URL: 
# https://github.com/ShahzadSarwar10/FULLSTACK-WITH-AI-BOOTCAMP-B1-MonToFri-2.5Month
# Explorer/blob/main/Week2/zameencom-property-data-By-Kaggle-Short.csv 
# It is Zameen.com REAL ESTATE – PK data. 


# 1. Load above CVS file above, into DataFrame variable , with Pandas, following columns 
# With “property_id” as Index column. 
# Print DataFrame.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file=pd.read_csv('Assignments\week_4\zameencom-property-data-By-Kaggle-Short.csv',delimiter=';')
df=pd.DataFrame(file)
# print(df)

# 2. Call following method/properties of DataFrame, print output and analyze the output. 
# .info() 
# .dtypes 
# .describe() 
# .shape

# ------------------------------------------------------------------------------

# print(df.info())
# print(df.shape)
# print(df.describe())
# print(df.dtypes)





# --------------------------------------------------------------------------
# 3. Assumption, that there is a Linear Regression relationship between 
# “bedrooms” being  as X and “price’ being as Y 
# Do To – convert DataFrame created above to array format, that is suited to SK Learn.
# 4. Slit data to 75% as training data and rest 25% as testing data. 
# 5. Train Linear regression Model, with train data in previous step.

sns.scatterplot(x=df['bedrooms'],y=df['price'], data=df)
sns.lineplot(x=df['bedrooms'],y=df['price'], data=df)
plt.show()

X=df[['bedrooms']]
y=df[['price']]


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.75,random_state=42)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

regressor.fit(X_train,y_train)

y_predict=regressor.predict(X_test)

df_predict=pd.DataFrame({"actual_value":y_test.squeeze(),"predictid_values":y_predict.squeeze()})
print(df_predict)

intercept = regressor.intercept_[0]     
slope = regressor.coef_[0][0]   

sns.scatterplot(x="actual_value",y="predictid_values", data=df_predict)
sns.lineplot(x="actual_value",y="predictid_values", data=df_predict)
plt.show()


bedrooms_series = df['bedrooms']

print("\nEstimated prices based on bedrooms:\n")
for beds in bedrooms_series:
    if beds <= 0 or beds > 8:
        continue 
    predicted_price = intercept + slope * beds
    print(f"Bedrooms: {beds} , Estimated Price: {predicted_price:.2f}")

