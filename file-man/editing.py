# XlUtils
# Bridge between xlrd and xlwt 


book = xlrd.open_workbook("xl/stores.xls", formatting_info=True)
book = xlutils.copy.copy(book)
book.get_sheet(0).write(0, 0 , "changed!")
book.save("stores_edited.xls")


