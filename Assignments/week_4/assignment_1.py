import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df=pd.read_csv('Assignments\week_4\Real_Estate_Sales_2001-2022_GL-Short.csv')
print(df.shape)
print(df.info())
print(df['Assessed Value'])
print(df['Sale Amount'])

sns.lineplot(x=df['Sale Amount'],y=df['Assessed Value'],data=df)
sns.scatterplot(x='Sale Amount', y='Assessed Value', data=df, color='red')
plt.show()

X=df[['Assessed Value']]
y=df[['Sale Amount']]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.8,random_state=42)

from sklearn.linear_model import LinearRegression
regression=LinearRegression()
regression.fit(X_train,y_train)

y_Predect=regression.predict(X_test)

predected_df=pd.DataFrame({"actual":y_test.squeeze(),"predected":y_Predect.squeeze()})
print(predected_df)

sns.scatterplot(x="actual", y="predected", data=predected_df, color="red")
sns.lineplot(x="actual", y="actual", data=predected_df, color="blue")  # perfect prediction line
plt.show()

slope=regression.coef_
intercept=regression.intercept_
print("slope" ,slope)
print("intercept",intercept)


from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
"""Now, we can calculate the MAE and MSE by passing the y_test (actual) and y_pred (predicted) to the methods. The RMSE can be calculated by taking the square root of 
the MSE, to to that, we will use NumPy's sqrt() method:
"""


mae = mean_absolute_error(y_test, y_Predect)
mse = mean_squared_error(y_test, y_Predect)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_Predect)
#We will also print the metrics results using the f string and the 2 digit precision after the comma with :.2f:

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')