#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import numpy as np
import pandas as pd


# In[2]:


tips = sns.load_dataset('tips')


# In[4]:


tips


# In[6]:


(/directly, using, the, plot, by, using, disbrition, plots)


# In[7]:


sns.residplot(x='total_bill',y='tips',data = tips, lowess =True)


# In[8]:


sns.residplot(x='total_bill',y='tip',data = tips, lowess =True)


# In[11]:


sns.jointplot(x='total_bill',y='tip',data = tips, kind='kde')


# In[12]:


sns.jointplot(x='total_bill',y='tip',data = tips, kind='hex')


# In[ ]:




