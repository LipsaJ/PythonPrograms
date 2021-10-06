#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:40:12 2021

@author: stlp
"""

#Python | Creating DataFrame from dict of narray/lists

import pandas as pd

#initialise dict of ndarrays
data = {'category': ["Array","stack","Queue"],
        'Marks': [10,16,9]}

df = pd.DataFrame(data)
print(df)

#initialise dict of ndarrays
data1 = {'category': ["Array","stack","Queue"],
        'student1': [10,16,9],
        'student2': [11,15,10]}

df1 = pd.DataFrame(data1)
print(df1.transpose())

# adding categories

df2 = pd.DataFrame(data1, index=["cat1","cat2","cat3"])
print(df2)

##----------------------------

## Creating Pandas dataframe using list of lists

data3 = [["Geeks", 20],["for", 10], ["geeks", 20]]
df3 = pd.DataFrame(data3, columns=["words","numbers"],index=["row1","row2","row3"])
print(df3)

data4 = [['DS', 'Linked_list', 10], ['DS', 'Stack', 9], ['DS', 'Queue', 7],
        ['Algo', 'Greedy', 8], ['Algo', 'DP', 6], ['Algo', 'BackTrack', 5], ]
df4 = pd.DataFrame(data4)
df4.columns = ["category","DataS","Questions"]
print(df4)
print(df4.transpose())
 