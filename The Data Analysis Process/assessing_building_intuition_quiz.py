#!/usr/bin/env python
# coding: utf-8

# # Assessing and Building Intuition Quiz
# Use the space below to explore `census_income_data.csv` to answer the quiz questions below.

# In[1]:


# Import pandas
import pandas as pd 

# Load census income data
df = pd.read_csv('census_income_data.csv')


# In[2]:


# Work to answer the quiz questions
df.shape


# In[3]:


df.types


# In[4]:


df.info


# In[5]:


df.type


# In[6]:


df.dtypes


# In[8]:


df.info


# In[9]:


df.info()


# In[10]:


df.unique()


# In[13]:


df.nunique()


# In[14]:


df.describe


# In[15]:


df.describe()


# In[ ]:




