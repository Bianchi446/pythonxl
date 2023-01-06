import pandas as pd
import excel 

values = excel.read(sheet_object, first_cell="A1", lasct_cell=None)
excel.write(sheet_object, values, first_cell="A1")


