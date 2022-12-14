#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import io
import sys
import maskpass

a=input("filename of your ans: ")
c = maskpass.advpass("Your UID: ")

excel1 = pd.read_excel("Sources/"+a)
excel2 = pd.read_excel("Sources/Finalanswers-release.xlsx")

MyAns=excel1.iloc[:-1,[1]].astype(str)
ModelAns=excel2.iloc[4:,[3]].reset_index().iloc[:,[1]]

def f(x):
    try:
        return round(float(x), 2)
    except:
        return x
ModelAns = ModelAns.applymap(f).astype(str)

MyAns = MyAns.applymap(f).astype(str)

a=MyAns[c].tolist()
b=ModelAns['Unnamed: 3'].astype(str).tolist()
count=0

print("--"*20)
print("Print Wrong Mismatched Answers")
print("--"*20)
for i in range(len(a)):
    if a[i]==b[i]:
        count+=1
            
    else:
        print(a[i],b[i])

print("--"*20)
print("Rough result:",(71-(len(a)-count)/71))

