import xlrd
import xlwt
from xlwt.Utils import cell_to_rowcol2
import xlutils
import excel 


# <1> Open the workbook to read cell values

book = xlrd.open_workbook('sample_data/stores.xlsx')

# <2> Get a list will all sheet names

book.sheet_names()

# <3> Loop through the sheet objects

for sheet in book.sheets():
    print(sheet.name)


