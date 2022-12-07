import datetime as dt
import xlsxwriter 
import excel 

# <1> Instantia a book
book = xlsxwriter.Workbook("xlswriter.xlsx")

#<2> specifies a sheet and give it a name

sheet = book.add_worksheet("Sheet1")


# <3> Write individual cells

sheet.write("A1", "Hello 1")
sheet.write(1, 0, "Hello 2")


#<4> formatting : fill color, alignment, border and font

formatting = book.add_format({"font_color": "#FF0000",
                            "bg_color": "#FFFF00",
                            "bold": True, "align": "center",
                            "border": 1, "border_color": "#FF0000"})
sheet.write("A3", "Hello 3", formatting)

# <5> Number formatting 

number_format = book.add_format({"num_format" : "0.00"})
sheet.write("A4", 3.3333, number_format)

# <6> Date formatting

date_format = book.add_format({"num_format" : "mm/dd/yy"})
sheet.write("A5", dt.date(2016, 10, 13), date_format)

# <7> formula

sheet.write("A6", "=SUM(A4, 2)")

# <8> Two-dimensional list

data = [[None, "North", "South"],
        ["Last Year", 2, 5],
        ["This Year", 3, 6]]
excel.write(sheet, data, "A10")


# <9> Chart 

chart = book.add_chart({"type": "column"})
chart.set_title({"name": "Sales per Region"})
chart.add_series({"name": "=Sheet1!A11",
                "categories": "=Sheet1!B10:C10",
                "values": "=Sheet1!B11:C11"})
chart.add_series({"name": "=Sheet1!A12",
                "categories": "=Sheet1!B10:C10",
                "values": "=Sheet1!B12:C12"})
chart.set_x_axis({"name": "Regions"})
chart.set_y_axis({"name": "Sales"})
sheet.insert_chart("A15", chart)


# Close the book

book.close()
