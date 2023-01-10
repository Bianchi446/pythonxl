import xlwt
from xlwt.Utils import cell_to_rowcol2
import datetime as dt
import excel

# <1> instantiate a workbook

book = xlwt.Workbook()

# <2> Add a sheet with a name
sheet = book.add_sheet("Sheet1")

# <3> Writing individual cells 

sheet.write(*cell_to_rowcol2("A1"), "Hello 1")
sheet.write(r=1, c=0, label="Hello 2")

# <4> Formating : Fill color, alignment, border and font

formatting = xlwt.easyxf("font : bold on, color blue;"
                         "align: horiz center;" 
                          "borders : top_color red, bottom_color red, "
                           "right_color red, left_color red,"
                            "left thin, right thin,"
                             "top thin, bottom thin;"
                            "pattern : pattern solid, fore_color yellow;")

sheet.write(r=2, c=0, label="Hello 3", style=formatting)

# <5>  Number formatting using Excel formatting strings 

number_format = xlwt.easyxf(num_format_str="0.00")
sheet.write(3, 0 , 3.3333, number_format)


# <6> Date formatting using Excel's formatting strings 

date_format = xlwt.easyxf(num_format_str="mm/dd/yy")
sheet.write(4, 0, dt.datetime(2012, 2, 3), date_format)


# <7> Formula 

sheet.write(5, 5, xlwt.Formula("SUM(C12, B12)"))

# <8> Two dimensional list (Using the excel.py module)

data = [[None, "Noth", "South"], 
        ["Last Year", 2, 5], 
        ["This year", 3, 6]]

excel.write(sheet, data, "A10")

# Saving

book.save("xl/xlwt.xls")
