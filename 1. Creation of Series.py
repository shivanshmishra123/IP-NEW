#!/usr/bin/env python
# coding: utf-8

# # Introduction:-
# Data structure is a collection of data values and operation that can be applied to that data. Enables efficient storage , retrieval and modificaiton.
# 
# 1)Series is a one dimensional array containing a sequence of value of any data type.
# 
# 2)When no. of index labels of a series does not match the no. of element, so we get a ValueError

# # 1)From Scalar Values 

# In[2]:


import pandas as pd
ser1=pd.Series([10,20,30])
ser1


# In[6]:


ser2=pd.Series(["Shivansh","Dev","Rishabh"])
ser2


# # 2)From Numpy Array

# In[6]:


import numpy as np
arr1=np.array(["Shivansh",10,"Dev",20,"Rishabh",30])
ser3=pd.Series(arr1)
ser3


# # 3) From a Dictionary
# 
# to remember that Key will go as a index value and value will be going as the correspoding entry

# In[9]:


dict1={"Shivansh":10,"Dev":20,"Rishabh":30}
ser4=pd.Series(dict1)
ser4


# In[ ]:





# In[ ]:





# In[ ]:




