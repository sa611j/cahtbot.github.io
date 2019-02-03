import webbrowser
import codecs
import xlrd 

message1 = """<!DOCTYPE html>
<html>
  <head>
    <style>
       /* Set the size of the div element that contains the map */
      #map {
        height: 400px;  /* The height is 400 pixels */
        width: 100%;  /* The width is the width of the web page */
       }
    </style>
    
  </head>
  <body>
    <h3>My Google Maps Demo</h3>
    <!--The div element for the map -->
  	<iframe id="mapImage"
  	  width="600"
  	  height="450"
  	  frameborder="0" style="border:0"
  	  src="https://www.google.com/maps/embed/v1/place?key=AIzaSyCZTfkaSU8xs1MLCks-X5Zx0xn_RnemtHk&q="""

message2 = """" allowfullscreen>
  	</iframe>
  </body>
</html>"""


loc = ("names.xlsx") 
  
wb = xlrd.open_workbook(loc) 

sheet = wb.sheet_by_name("Sheet1")

for i in range(sheet.nrows):
# for i in range(10):
	webName = str(sheet.cell(i,1).value)
	f = open('restaurant/' + webName + '.html','w',encoding="utf-8")
	place = sheet.cell(i,0).value
	allName = message1 + place +  message2
	f.write(allName)
	f.close()

webbrowser.open_new_tab('restaurant/' + webName + '.html')