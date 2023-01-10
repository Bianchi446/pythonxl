import xlsxwriter
import pandas as pd

# Formatting index/headers with XlsxWriter

with pd.ExcelWriter("formatting_xlsxwriter.xlsx", engine="xlsxwriter") as writer:

    # Write out the df with the default formatting to A1

    df.to_excel(writer, startrow=0, startcol=0)

    # Write out the df with custom index/header formatting to A6

    startrow, startcol = 0,5 

    df.to_excel(writer, header=False, index=False, startrow=startrow + 1, startcol=startcol + 1)

    # <1> Get the book and the sheet object and create a style object

    book = writer.book 
    sheet = writer.sheets["Sheet1"]
    style = book.add_format({"bg_color" : "#D9D9D9"})

    # <2>  Write out the styled column headers
    
    for i, col in enumerate(df.columns):
        sheet.write(startrow, startcol + i + 1, col, style)


    # <3> Write out the styled index

    index = [df.index.name if df.index.name else None] + list(df.index)
    for i, row in enumerate(index):
        sheet.write(startrow + i, startcol, row, style)






















