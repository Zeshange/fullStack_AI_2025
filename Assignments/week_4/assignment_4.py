import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
file_data=pd.read_csv('Assignments\week_4\Startups .csv')


df=pd.DataFrame(file_data)
# print(df)
X=df[['R&D Spend','Administration','Marketing Spend']]
y=df['Profit']
print(X)
print(y)

variables=['R&D Spend','Administration','Marketing Spend']
for var in variables:
    # plt.figure()
    sns.regplot(x=var,y=y, data=df)
    plt.show()



X_train,X_test,y_train,y_test=train_test_split(X,y, random_state=42, test_size=0.1)



Lregration=LinearRegression()
Lregration.fit(X_train,y_train)

y_predict=Lregration.predict(X_test)

df_predict=pd.DataFrame({'actual_y':y_test , "predicted_y":y_predict})

sns.scatterplot(x='actual_y',y='predicted_y',data=df_predict)
sns.lineplot(x='actual_y',y='predicted_y',data=df_predict)
plt.show()
print(df_predict)

print(Lregration.coef_)
print(Lregration.intercept_)


from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

import numpy as np

mae = mean_absolute_error(y_test, y_predict)
mse = mean_squared_error(y_test, y_predict)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_predict)


print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')
print(f'R2 Score: {r2:.2f}')