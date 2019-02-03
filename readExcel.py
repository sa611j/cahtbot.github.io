# Program extracting all columns 
# name in Python 
import xlrd 

import codecs

loc = ("data.xlsx") 
  
wb = xlrd.open_workbook(loc) 

#################################
# sheet_names = wb.sheet_names()
# f = codecs.open("out.txt","w","utf8")
# for name in sheet_names:
# 	f.write(name + "\n")
# f.close() 
################################

sheet_name = "ぐるなび"
sheet = wb.sheet_by_name(sheet_name)

f = codecs.open("outX.xlsx","w","utf8")

for i in range(2,sheet.nrows):
	# for j in range(sheet.ncols):
	name = str(sheet.cell(i,4).value) + ","
	
	if sheet.cell(i,11).value == xlrd.empty_cell.value:
		name +=  str(sheet.cell(i,10).value)
	else:
		name += str(sheet.cell(i,11).value)

	f.write(name)
	f.write("\n")
		
f.close() 
