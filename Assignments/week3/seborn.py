import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


file_csv=pd.read_csv('Assignments\week3\RealEstate-USA (1).csv' , dtype={'price': 'int'})
df=pd.DataFrame(file_csv)


# filterdf =  df.sort_values("price").head(10)
# sns.lineplot(x='city', y='price', data=filterdf)

# sns.lineplot(x='city', y='price', data=df.nlargest(10,"price"))
# plt.show()

# sns.lineplot(x='city', y='price', data=df )
# plt.show() 

# sns.catplot(x='city', y='price', data=df)
# plt.show()


# sns.kdeplot(x='zip_code', y='price', data=df)
# plt.show()


# sns.scatterplot(x='zip_code', y='price', data=df)
# plt.show()

# sns.barplot(x='zip_code', y='price', data=df)
# plt.show()

# sns.set_theme()
# sns.lineplot(x='zip_code', y='price', data=df)
# plt.show()


# sns.set_theme(style="whitegrid", palette="pastel")
# sns.lineplot(x='zip_code', y='price', data=df)
# plt.show()


# sns.set_theme(style="dark", palette=None)
# sns.lineplot(x='zip_code', y='price', data=df)
# plt.show()

# sns.set_theme(style="white", palette=None)
# sns.lineplot(x='zip_code', y='price', data=df)
# plt.show()


# custom_params = {"axes.spines.right": False, "axes.spines.top": False}
# sns.set_theme(style="ticks", rc=custom_params)
# sns.lineplot(x='zip_code', y='price', data=df)
# plt.show()




# sns.lineplot(data=df, x="city", y="price")

# # Set x-tick labels to only show each city name once
# # Get the first occurrence of each city
# unique_labels = df["city"].drop_duplicates().values
# tick_positions = df.groupby("city").ngroup().drop_duplicates().values

# plt.xticks(ticks=tick_positions, labels=unique_labels, rotation=90)
# plt.tight_layout()
# plt.show()


# sns.lineplot(data=df, x="house_size", y="price")
# plt.show()

sns.lineplot(data=df, x="zip_code", y="price")
plt.show()