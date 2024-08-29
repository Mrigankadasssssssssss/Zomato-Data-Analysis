#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sns


# In[2]:


df = pd.read_csv("Zomato data .csv")


# In[3]:


df


# handle rate (only printing numerator)

# In[4]:


def handleRate(val):
    val = str(val).split('/')
    val = val[0]
    return float(val)
df['rate'] = df['rate'].apply(handleRate)
df.headd()


# ## Q1) Type Of Resturant

# In[5]:


df.head(10)


# In[7]:


sns.countplot(x=df['listed_in(type)'])
pt.xlabel('type of resturant')


# ### ans. majority of the resturant fall under the dining category.

# ## Q2) How Many Votes?

# In[8]:


grouped_data = df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes':grouped_data})
pt.plot(result,c='violet',marker='o')
pt.xlabel('Types of Resturant',c='green',size='20')
pt.ylabel('Votes',c='green',size='20')


# ### ans. Dining resturant has recieved max vote

# ## Q3) What are the major rating

# In[13]:


pt.hist(df['rate'],bins=5)
pt.title("Major rating Lie On...")
pt.show()


# ### ans. Majority rating lies on from 3.50 to 4.00

# ## Q4) Avg Spending on each order by couples?

# In[14]:


couple_spending = df['approx_cost(for two people)']
sns.countplot(x=couple_spending)


# ### ans. The majority of the couples orders the food of avg cost Rs. 300

# ## Q5) Which mode(online/offline) recieves maximum Rating?

# In[16]:


df.head()


# In[17]:


pt.figure(figsize=(6,6))
sns.boxplot(x='online_order',y='rate',data=df)


# ### ans. online order recieves more rating than offline order

# ## Q6) Which type of resturant recieves more offline order?

# In[19]:


pivotTable = df.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivotTable,annot=True,cmap="YlGnBu",fmt='d')
pt.title("Heat Map")
pt.xlabel("Online Order")
pt.ylabel("listed_in(type)")
pt.show()


# ### ans. Dining resturant serves more offline orders, whereas Buffet,cafes,others are serving more online orders

# In[ ]:




