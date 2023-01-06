import xlrd
import xlwt
from xlwt.Utils import cell_to_rowcol2
import xlutils
import excel


book = xlrd.open_workbook("xl/stores.xls")

print(book.sheet_names())

for sheet in book.sheets():
    print(sheet.name)


# Get a sheet object  by name or index

sheet = book.sheet_by_index(0)
sheet2 = book.sheet_by_name("2019")

print(sheet)
print(sheet2)

print(sheet.nrows)
print(sheet.ncols)


# Reading value of cells using cell indices

print(sheet.cell(*cell_to_rowcol2("D4")).value)
