import pandas as pd
import openpyxl 

df = pd.DataFrame({"col1" : [1, -2], "col2" : [-3, 4]}, 
                    index=["row1", "row2"])

df.index.name = "ix"
print(df)
