import numpy as np
import pandas as pd
import datetime  as dt

data=[[dt.datetime(2020,1,1, 10, 13), 2.222, 1, True],
    [dt.datetime(2020,1,2), np.nan, 2, False],
    [dt.datetime(2020,1,2), np.inf, 3, True]]


df = pd.DataFrame(data=data, columns=["Dates", "Integers", "Float", "Boolean"])

df.index.name = "index"

print(df)


# Converting the data frame to an excel file 

df.to_excel("written_with_pandas.xlsx", sheet_name="Output", startrow=1, startcol=1, index=True, header=True, na_rep="<NA>", inf_rep="<INF>")


