import pandas as pd

# Converter function for wrong cell data type


def fix_missing(x):
    return False if x in ["", "MISSING"] else x   

df = pd.read_excel("xl/stores.xlsx", sheet_name="2019", usecols="B:C,F", header=None, skiprows=1, converters={"Flagship" : fix_missing})

print(df)


# Using the ExcelFile class in action :

with pd.ExcelFile("xl/stores.xls") as f:
    df1 = pd.read_excel(f, "2019", skiprows=1, usecols="B:F", nrows=2)
    df2 = pd.read_excel(f, "2020", skiprows=1, usecols="B:F", nrows=2)


