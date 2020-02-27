# Writing to an excel
import xlwt 
from xlwt import Workbook 

# Workbook is created 
wb = Workbook() 
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

#writing!!
sheet1.write(1, 1, "Hello fai")


#close
wb.save('cpu_time_scheduling.xls') 