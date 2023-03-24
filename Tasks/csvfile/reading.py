import xlrd
loc = ("/home/madhu/Downloads/Salary-Calculation-Sheet-and-Salary-Slip-Template-in-Excel (1).xlsm")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
for i in range(sheet.ncols):
    print(sheet.cell_value(0, i))