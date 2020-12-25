#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns                       
import matplotlib.pyplot as plt             
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[2]:


df = pd.read_csv("car_data.csv")
# To display the top 5 rows 
df.head(5)  


# In[5]:


df.tail(5)


# In[6]:


df.dtypes


# In[7]:


df = df.drop(['Engine Fuel Type', 'Market Category', 'Vehicle Style', 'Popularity', 'Number of Doors', 'Vehicle Size'], axis=1)
df.head(5)


# In[8]:


df = df.rename(columns={"Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })
df.head(5)


# In[9]:


df.shape


# In[10]:


duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)


# In[11]:


df.count()     


# In[12]:


df = df.drop_duplicates()
df.head(5)


# In[13]:


df.count()


# In[14]:


print(df.isnull().sum())


# In[15]:


df = df.dropna()    # Dropping the missing values.
df.count()


# In[16]:


print(df.isnull().sum())   # After dropping the values


# In[17]:


sns.boxplot(x=df['Price'])


# In[18]:


sns.boxplot(x=df['HP'])


# In[19]:


sns.boxplot(x=df['Cylinders'])


# In[20]:


Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)


# In[21]:


df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape


# In[22]:


df.Make.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("Number of cars by make")
plt.ylabel('Number of cars')
plt.xlabel('Make');


# In[23]:


plt.figure(figsize=(10,5))
c= df.corr()
sns.heatmap(c,cmap="BrBG",annot=True)
c


# In[24]:


fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(df['HP'], df['Price'])
ax.set_xlabel('HP')
ax.set_ylabel('Price')
plt.show()


# In[ ]:




