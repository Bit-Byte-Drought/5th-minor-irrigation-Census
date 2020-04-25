#!/usr/bin/env python
# coding: utf-8

# In[1]:


def clean(df):
    df = df.sort_values(by = ['State', 'District', 'Block/Tehsil', 'Village'], ignore_index = True)
    def add(x):
        for i in range(4):
            x[i] = x[i].strip()
        return x[0] + '_' + x[1] + '_' + x[2] + '_' + x[3]
    df.index = df.iloc[:,:4].apply(add, axis = 1)
    df.index.name = 'State_District_Block/Tehsil_Village'
    df = df.drop(columns = ['State', 'District', 'Block/Tehsil', 'Village'])
    return df

