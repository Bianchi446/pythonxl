import numpy as np
import pandas as pd 

msft = pd.read_csv("csv/MSFT.csv")

msft.info()

msft.loc[:, "date"] = pd.to_datetime(msft["Date"])
print(msft)


# Working with time zones 

msft_close = msft.loc[:, ['Adj close']].copy()
msft_close.index = msft_close.index + pd.DateOffSet(hours=16)
msft_close.head(2)

print(msft_close)


