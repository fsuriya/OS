################### Import ###############################
# Writing to an excel
import xlwt 
from xlwt import Workbook 

# Random
import random

################### Global variable ######################
numOfProcess = 0        #Number of Process
p1 = []                 #number of process time 2-8   ms
p2 = []                 #number of process time 20-30 ms
p3 = []                 #number of process time 35-40 ms
tatalProcess = []       #p1+p2+p3
command = ""
case = 0

################### Function #############################
def GenProcessList(command, numOfProcess, p1, p2, p3):

    print(command, numOfProcess, p1, p2, p3)

def WriteHeaderSheet(command, p1, p2, p3, tatalProcess, case):
    #arrival time
    sheet1.write(0, 0, "Using Arrival Time")
    if command == "Y":
        sheet1.write(0, 1, "Yes")
    elif command == "N":
        sheet1.write(0, 1, "No")
    
    #number of case
    sheet1.write(1, 0, "Number of case")
    sheet1.write(1, 1, case)

    #number of process
    sheet1.write(3, 0, "number of process")
    sheet1.write(4, 0, "process 1")
    sheet1.write(5, 0, "process 2")
    sheet1.write(6, 0, "process 3")
    sheet1.write(7, 0, "total")

    for x in range(case):
        sheet1.write(3, x+1, "case"+str(case+1))
        sheet1.write(4, x+1, p1[case])
        sheet1.write(5, x+1, p2[case])
        sheet1.write(6, x+1, p3[case])
        sheet1.write(7, x+1, tatalProcess[case])
    
    #percent of process
    sheet1.write(9, 0, "percent of process")
    sheet1.write(10, 0, "process 1")
    sheet1.write(11, 0, "process 2")
    sheet1.write(12, 0, "process 3")

    for x in range(case):
        sheet1.write(9, x+1, "case"+str(case+1))
        sheet1.write(10, x+1, (p1[case]/tatalProcess[case])*100)
        sheet1.write(11, x+1, (p2[case]/tatalProcess[case])*100)
        sheet1.write(12, x+1, (p3[case]/tatalProcess[case])*100)


#################### main ################################
# Workbook is created 
wb = Workbook() 
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

while command != "Y" and command != "N" :
    command = input("Process with Arrival Time (Y/N) : ")
    command = command.upper()

case = int(input("Enter number of case : "))
for x in range(case):
    p1.append(random.randrange(0,100)) 
    p2.append(random.randrange(0,100)) 
    p3.append(random.randrange(0,100))
    tatalProcess.append(p1[x]+p2[x]+p3[x])

#GenProcessList(command, numOfProcess, p1, p2, p3)
WriteHeaderSheet(command, p1, p2, p3, tatalProcess, case)

wb.save('xlwt example.xls') 