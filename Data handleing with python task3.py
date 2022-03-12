#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Step 1. Import the necessary libraries Step
import pandas as pd
import numpy as np


# In[2]:


#step 2. Import the dataset chipotle.tsv & Assign it to a variable called chipo. 
chipo=pd.read_table('C:/Users/gagan/Desktop/DA_Test_March 2022/DA_Test_March 2022/Python Data Handling/chipotle.tsv')
chipo.head()


# In[3]:


chipo.tail()


# In[4]:


chipo.info()


# In[5]:


#Converting the column to proper numeric type data before filtering. 
chipo['item_price']=chipo['item_price'].str.replace('$','',regex=True)
chipo['item_price']=pd.to_numeric(chipo['item_price'])
chipo['item_price']


# In[6]:


#another way to change the data type
#chipo['item_price']=chipo['item_price'].str.replace('$','').str.replace(',','')
#chipo['item_price']=pd.to_numeric(chipo['item_price'])
#chipo['item_price']


# In[7]:


chipo.head()


# In[8]:


chipo['item_price'].isnull().sum()


# In[9]:


#Step 4. How many products cost more than $10.00?
itemprice =chipo['item_price']
itemprice


# In[10]:


item_price_more_than10 = itemprice>10


# In[11]:


item_price_more_than10.value_counts()


# In[12]:


item_price_more_than10.sum()


# In[13]:


#Step 5. What is the price of each item? 
chipo


# In[14]:


a=chipo.drop_duplicates(subset='item_name')
a


# In[15]:


new=a.drop(['order_id','quantity','choice_description'],axis=1)
new


# In[16]:


#i tried this way but it didn't gave me the correct values  
#a=chipo['item_name'].unique()
#a
#b=chipo['item_price'].unique()
#b
#a=a.tolist()
#a
#b=b.tolist()
#b
#new=pd.DataFrame(data=[a,b])
#new
#new=new.T
#new


# In[17]:


#Step 6. Sort by the name of the item 
sort1=chipo.sort_values(by='item_name')
sort1


# In[18]:


sort2=new.sort_values(by='item_name')
sort2


# In[19]:


#Step 7. What was the quantity of the most expensive item ordered? 
chipo.head()


# In[20]:


chipo['item_price'].max()


# In[21]:


m=chipo[chipo['item_price']==chipo['item_price'].max()]
m


# In[22]:


#Step 8. How many times were a Veggie Salad Bowl ordered?
chipo['item_name'].value_counts()


# In[23]:


count=0
for i in chipo['item_name']:
    if i =='Veggie Salad Bowl':
        count+=1
print(count)


# In[24]:


chipo[chipo['item_name']=='Veggie Salad Bowl']['item_name'].value_counts()


# In[25]:


#Step 9. How many times people ordered more than one Canned Soda?
chipo.head()


# In[26]:


chipo[chipo['item_name']=='Canned Soda']['item_name'].value_counts()


# In[27]:


cd=chipo[(chipo['item_name']=='Canned Soda') & (chipo['quantity']>=2)]
cd


# In[28]:


len(cd)

