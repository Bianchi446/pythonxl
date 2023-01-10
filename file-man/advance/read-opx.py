import openpyxl
import pandas as pd

book = openpyxl.load_workbook('xl/big.xlsx', data_only=True, read_only=True, keep_links=False)

book.close()

