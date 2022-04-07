import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\praha\\OneDrive\\Desktop\\Ex-04-EDA-main\\Ex-04-EDA-main\\supermarket.csv")
  df
  df.isnull().sum()
cols=[' Invoice ID','Branch','City','Customer type','Gender','Product line','Unit price','Quantity','Tax 5% ','Total','Data','Time
pd.columns=cols
  df.head()
  df.isnull().sum()
for col in df.columns:
  print('{} : {}'.format(col,df[col].unique()))
for col in df.columns:
  df[col].replace({'?':np.nan},inplace=True)
      df.head()
      df.isnull().sum()
      sns.heatmap(df.isnull(),cbar=False,cmap='viridis')      
plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cbar=True,annot=True,cmap='Blues')
      plt.figure(figsize=(10,10))
plt.scatter(x='Tax 5%',y='Payment',data=df)
plt.xlabel('Tax')
plt.ylabel('Price')
      sns.histplot(df.Quantity,bins=10)
      df.Total.value_counts()
      sns.boxplot(x='Unit price',y='Quantity',data=df)
      

      
