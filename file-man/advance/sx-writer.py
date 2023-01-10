import xlsxwriter
import pandas as pd

book = xlsxwriter.Workbook("xlsxwriter_optimized.xlsx", options={"constant_memory": True})

sheet = book.add_worksheet()

# Producing 1000 x 20 cells: 

for row in range(1000):
    sheet.write_row(row, 0, list(range(200)))
book.close()
