# Program extracting all columns 
# name in Python 
import xlrd 

import codecs

import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('names.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0

loc = ("data.xlsx") 
  
wb = xlrd.open_workbook(loc) 


sheet_name = "ぐるなび"
sheet = wb.sheet_by_name(sheet_name)

for i in range(2,sheet.nrows):
	# for j in range(sheet.ncols):
	name = str(sheet.cell(i,4).value) + ","
	
	if sheet.cell(i,11).value == xlrd.empty_cell.value:
		name +=  str(sheet.cell(i,10).value)
	else:
		name += str(sheet.cell(i,11).value)

	worksheet.write(row, col, name)
	row += 1
workbook.close()