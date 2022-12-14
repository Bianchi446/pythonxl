from pathlib import Path
import pandas as pd
import numpy as np 

def fix_missing(x):
    return False if x in ["", "MISSING"] else x

df = pd.read_excel("sales_data/stores.xlsx", sheet_name="2019", skiprows=1, usecols="B:F", converters={"Flagship" : fix_missing})

print(df)



# Reading a list of excel sheets 

sheets = pd.read_excel("sales_data/stores.xlsx", sheet_name=["2019", "2020"], skiprows=1, usecols=["Store", "Employees"])

print(sheets["2019"].head(2))


# Column headers

df = pd.read_excel("sales_data/stores.xlsx", sheet_name=0, skiprows=2, skipfooter=3, usecols="B:C,F", header=None, 
                    names=["Branch", "Employee_Count", "Is_Flagship"])

print(df)


# ExcelFile class 

with pd.ExcelFile("sales_data/stores.xlsx") as f:
    df1 = pd.read_excel(f, "2019", skiprows=1, usecols="B:F", nrows=2)
    df2 = pd.read_excel(f, "2020", skiprows=1, usecols="B:F", nrows=2)

print(df1)
print(df2)


# ExcelFile gives you access to the name of all sheets 

stores = pd.ExcelFile('sales_data/stores.xlsx')
print(stores.sheet_names)
