#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 09:03:15 2021

@author: stlp
"""
import pandas as pd
# Convert list of nested dictionary into Pandas dataframe

list1 = [
        {
        "Student": [{"Exam": 90, "Grade": "a"},
                    {"Exam": 99, "Grade": "b"},
                    {"Exam": 97, "Grade": "c"},
                   ],
        "Name": "Paras Jain"
        },
        {
        "Student": [{"Exam": 89, "Grade": "a"},
                    {"Exam": 80, "Grade": "b"}
                   ],
        "Name": "Chunky Pandey"
        }
       ]

print("Actual list\n")
print(list1)
rows = []

for data in list1:
    st_row = data["Student"]
    nm_row = data["Name"]
    
    for row in st_row:
        row["Name"] = nm_row
        rows.append(row)
        
print("\nnew list with name tags\n")
print(rows)
df = pd.DataFrame(rows)

print("\ndataframe with name column\n")
print(df)
    
# using pivot table

df = df.pivot_table(index="Name", columns=["Grade"],values=["Exam"]).reset_index()
print("\ndataframe after pivoting\n")
print(df)    

print("\ndataframe after column names\n")
df.columns = ['Name','Maths','Physics','Bio']
print(df)
