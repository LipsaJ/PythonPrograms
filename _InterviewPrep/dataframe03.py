#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 22:57:26 2021

@author: stlp
"""


import pandas as pd

# Creating a Pandas dataframe using list of dictionaries

data3 = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list'},
        {'Geeks':10, 'For': 20, 'geeks': 30}] 

df3 = pd.DataFrame.from_dict(data3)
print(df3)

df4 = pd.DataFrame(data3, index = ['ind1','ind2'])
print(df4)

df5 = pd.DataFrame(data3, index = ['ind1','ind2'],columns =['Geeks', 'For'])
print(df5)

# Creating a Pandas dataframe using list of tuples

data = [("peter",2,31),
        ("quill",7,39),
        ("john",8,29),
        ("Robb",6,22),
        ("Eugene",5,40),]

df = pd.DataFrame(data, columns = ["Names","GPA","Maths"])
print(df)

df1 = pd.DataFrame.from_records(data, columns = ["Names","GPA","Maths"])
print(df1)

data2 = [
('Age', [18, 15, 17, 18, 17]),
('Team', ['A', 'B', 'A', 'C', 'B']),
('Score', [7, 6, 8, 7, 5]),
]

df2 = pd.DataFrame.from_dict(data2)
print(df2)