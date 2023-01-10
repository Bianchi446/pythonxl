import openpyxl
import pandas as pd

book = openpyxl.Workbook(write_only=True)

# With write_only=True, book.active doesn't work

sheet = book.create_sheet()

# Produce a sheet with 1000 x 200 cells

for fow in range(1000):
    sheet.append(list(range(200)))
book.save("openpyxl_optimized.xlsx")

