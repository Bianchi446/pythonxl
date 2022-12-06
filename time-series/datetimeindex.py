import pandas as pd
import numpy as np
pd.options.plotting.backend = 'plotly'

# Creates a daily frequency of 4 periods

daily_index = pd.date_range("2020-02-28", periods=4, freq='D')
print(daily_index)


# Construct a DataFrame based on weekly index

weekly_index = pd.date_range("2020-01-01", "2020-01-31", freq="W-SUN")

df = pd.DataFrame(data=[21, 15, 33, 44], columns=["visitors"], index=weekly_index)

print(df)


# Reading CSV

msft = pd.read_csv("csv/MSFT.csv")

msft.info()

msft.loc[:, 'Date'] = pd.to_datetime(msft["Date"])

print(msft.dtypes)


#    
