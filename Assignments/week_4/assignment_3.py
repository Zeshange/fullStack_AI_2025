# Task 3- Linear Regression SK Learn implementation: 
# A Simple Task for Linear Regression SK Learn implementation: 
# Dataset under discussion - Sample URL: 
# https://github.com/ShahzadSarwar10/FULLSTACK-WITH-AI-BOOTCAMP-B1-MonToFri-2.5Month
# Explorer/blob/main/DataSetForPractice/number-of-registered-medical-and-dental-doctors-by-gender
# in-pakistan%20(1).csv 
# It is medical industry – PK data. 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Load above CVS file above, into DataFrame variable , with Pandas, following columns 
# With “Years” as Index column. 
# Print DataFrame.    


file=pd.read_csv('Assignments\\week_4\\number-of-registered-medical-and-dental-doctors-by-gender-in-pakistan (1).csv',delimiter=',')
df=pd.DataFrame(file)
print(df)


# 2. Call following method/properties of DataFrame, print output and analyze the output. 
# .info() 
# .dtypes 
# .describe() 
# .shape

print(df.info())
print(df.shape)
print(df.describe())
print(df.dtypes)

sns.scatterplot(x=df['Female Doctors'],y=df['Female Dentists'],data=df)
sns.lineplot(x=df['Female Doctors'],y=df['Female Dentists'],data=df)
plt.show()
# 3. Assumption, that there is a Linear Regression relationship between 
# “Female Doctors” being  as X and “Female Dentists’ being as Y 
# Do To – convert DataFrame created above to array format, that is suited to SK Learn. 
# 4. Slit data to 70% as training data and rest 30% as testing data. 
# 5. Train Linear regression Model, with train data in previous step. 
# 6. Find and print your “intercept” 
# 7. Find and print your “slope” 

from sklearn.model_selection import train_test_split

df['Female Doctors'] = df['Female Doctors'].str.replace(',', '', regex=False).astype(float)
df['Female Dentists'] = df['Female Dentists'].str.replace(',', '', regex=False).astype(float)
X=df[['Female Doctors']]
y=df[['Female Dentists']]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.70,random_state=42)

from sklearn.linear_model import LinearRegression
regrassor=LinearRegression()
regrassor.fit(X_train,y_train)


intercept=regrassor.intercept_[0]
slope=regrassor.coef_[0][0]

print(intercept)
print(slope)



y_predict=regrassor.predict(X_test)

y_prediction=pd.DataFrame({'actual':y_test.squeeze(),'predicted':y_predict.squeeze()})
print(y_predict)

sns.scatterplot(x='actual',y='predicted',data=y_prediction)
sns.lineplot(x='actual',y='predicted',data=y_prediction)
plt.show()

df['Female Doctors'] = df['Female Doctors'].astype(str).str.replace(',', '', regex=False).astype(float)
femail_doctor=df['Female Doctors']
def cal_dantest(f_doc,inter,slop):
    return inter + slop * f_doc

for f_doctor in femail_doctor:
    prediction=cal_dantest(f_doctor,intercept,slope)
    print(f"femail doctor:{f_doctor},predicted_femail_dantist:{prediction:.2f}")