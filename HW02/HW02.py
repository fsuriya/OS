################### Import ###############################
# Writing to an excel
import xlwt 
from xlwt import Workbook 
# Random
import random

import PageRep

#################### main ################################
# Workbook is created 
wb = Workbook() 
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

###########Gen data
rangeOfData = 7
dataList = []
dataList10 = []
dataList20 = []
dataList30 = []
dataList40 = []
dataList50 = []
#dataList size = 10
for i in range(10):
    dataList10.append(random.randrange(rangeOfData))
#dataList size = 20
for i in range(20):
    dataList20.append(random.randrange(rangeOfData))
#dataList size = 30
for i in range(30):
    dataList30.append(random.randrange(rangeOfData))
#dataList size = 40
for i in range(40):
    dataList40.append(random.randrange(rangeOfData))
#dataList size = 50
for i in range(50):
    dataList50.append(random.randrange(rangeOfData))
#shuffle
random.shuffle(dataList10)
random.shuffle(dataList20)
random.shuffle(dataList30)
random.shuffle(dataList40)
random.shuffle(dataList50)
dataList.append(dataList10)
dataList.append(dataList20)
dataList.append(dataList30)
dataList.append(dataList40)
dataList.append(dataList50)
########################################################

########## Write Work book header
for i in range(5):
    sheet1.write(i, 0, "Data "+str(i+1))
    for j in range(len(dataList[i])):
        sheet1.write(i, j+1, dataList[i][j])

for x in range(len(dataList)):
    sheet1.write(6+(x*6), 0, "Data List :" + str(x+1))
    sheet1.write(7+(x*6), 0, "Number of frame")
    sheet1.write(8+(x*6), 0, "FIFO")
    sheet1.write(9+(x*6), 0, "Optimal")
    sheet1.write(10+(x*6), 0, "RLU")
    for i in range(1,9):
        sheet1.write(7+(x*6), i, str(i))
        sheet1.write(8+(x*6), i, PageRep.FIFO(dataList[x],i))
        sheet1.write(9+(x*6), i, PageRep.Optimal(dataList[x],i))
        sheet1.write(10+(x*6), i, PageRep.RLU(dataList[x],i))

wb.save('page_rep.xls') 