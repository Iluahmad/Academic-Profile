# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:25:56 2024

@author: Ahmad Ilu
"""

import pandas as pd

data = pd.read_excel(r"C:\Users\Ahmad Ilu\Downloads\food_Prices.xlsx", sheet_name= "Sheet2")
print(data)
print(data.head(5))
data
data.info()