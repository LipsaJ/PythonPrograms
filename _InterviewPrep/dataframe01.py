# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

# Q1: Make a Pandas DataFrame with two-dimensional list | Python

# List1  
lst = [['Geek', 25], ['is', 30], 
       ['for', 26], ['Geeksforgeeks', 22]] 

# now creating dataframe

df = pd.DataFrame(lst, columns = ['Tag','Number'])
print(df)

lst2 = ['geek','is','for','geekforgeeks']

df2 = pd.DataFrame(lst2, columns=['words'])
print(df2)

# List1  
lst3 = [['tom', 'reacher', 25], ['krish', 'pete', 30], 
       ['nick', 'wilson', 26], ['juli', 'williams', 22],
       ['dom', 'reacher', 29], ['krishna', 'patel', 33]]

df3 = pd.DataFrame(lst3, columns=['fname','lname','age'])
print(df3)
                   