import pandas as pd
import openpyxl

with pd.ExcelFile('xl/stores.xlsx', engine="openpyxl") as xlfile:
    # Read a DataFrame

    df = pd.read_excel(xlfile, sheet_name="2020")

    # Get the OpenPyXl  workbook object

    book = xlfile.book

    sheet = book["2019"]
    value = sheet["B3"].value

    with pd.ExcelWriter("pandas_and_openpyxl.xlsx", engine="openpyxl") as writer:
        df = pd.dataFrame({"Col1" : [1, 2, 3, 4], "col2": [5, 6, 7, 8]})

        # Write a dataFrame
        df.to_excel(writer, "Sheet1", startrow=4, startcol=2)

        # Get the openpyxl workbook and sheet objects

        book = writer.book
        sheet = writer.sheets["Sheet1"]

        #

        sheet["B2"].value = "This is a title"




