################### Import ###############################
# Writing to an excel
import xlwt 
from xlwt import Workbook 
# Random
import random

################### Global variable ######################
p1 = 0                  #number of process time 2-8   ms
p2 = 0                  #number of process time 20-30 ms
p3 = 0                  #number of process time 35-40 ms
command = ""            #i will be create in future part "LOL"
case = 0                #number of test case
processList = []        #collect process list from def generateListData
FCFSTime = 0.0              #avg wait time first come first search
SJFTime = 0.0               #avg wait time shortest job first 
RRTime = 0.0                #avg wait time round robin

################### Function #############################
def WriteHeaderSheet(command, case):
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
    
    #percent of process
    sheet1.write(9, 0, "percent of process")
    sheet1.write(10, 0, "process 1")
    sheet1.write(11, 0, "process 2")
    sheet1.write(12, 0, "process 3")

    #average waiting time
    sheet1.write(14, 0, "average waiting time")
    sheet1.write(15, 0, "process 1")
    sheet1.write(16, 0, "process 2")
    sheet1.write(17, 0, "process 3")

    #Data list
    sheet1.write(19, 0, "Data list")
    sheet1.write(20, 0, "No. case")
    sheet1.write(21, 0, "Sum time process")

def WriteDataSheet(case, p1, p2, p3, FCFSTime, SJFTime, RRTime, processList, sumTime):
    #number of process
    sheet1.write(3, case+1, "case "+str(case+1))
    sheet1.write(4, case+1, p1)
    sheet1.write(5, case+1, p2)
    sheet1.write(6, case+1, p3)
    sheet1.write(7, case+1, p1+p2+p3)
    
    #percent of process
    sheet1.write(9, case+1, "case "+str(case+1))
    sheet1.write(10, case+1, (p1/(p1+p2+p3))*100)
    sheet1.write(11, case+1, (p2/(p1+p2+p3))*100)
    sheet1.write(12, case+1, (p3/(p1+p2+p3))*100)

    #average waiting time
    sheet1.write(14, case+1, "case "+str(case+1))
    sheet1.write(15, case+1, FCFSTime)
    sheet1.write(16, case+1, SJFTime)
    sheet1.write(17, case+1, RRTime)

    #Data list
    sheet1.write(20, case+1, "case "+str(case+1))
    sheet1.write(21, case+1, sumTime)
    for x in range(len(processList)):
        sheet1.write(22+x, case+1, processList[x])
        sumTime += processList[x]


def generateListData(p1, p2, p3, processList, sumTime):
    numProcess = random.randrange(20,61)                  #20 to 60 processes
    for x in range(numProcess):                                   #generate process = numProcess time
        y = random.randrange(0,3)                          #random process
        if y == 0:
            processList.append(random.randrange(2,9))      #process time 2 to 8 ms
            p1+=1
        elif y == 1:
            processList.append(random.randrange(20,31))    #process time 20 to 31 ms
            p2+=1
        elif y == 2:
            processList.append(random.randrange(35,40))    #process time 20 to 31 ms
            p3+=1
        sumTime += processList[x]

    return (p1,p2,p3),processList,sumTime

def FCFS(FCFSTime, processList, numProcess):
    temp = 0
    for x in range(len(processList)):
        FCFSTime += temp
        temp += processList[x]
    FCFSTime = FCFSTime/numProcess
    return FCFSTime

def SJF(SJFTime, tempprocessList, numProcess):
    temp = 0
    for x in range(len(tempprocessList)):
        SJFTime += temp
        temp += min(tempprocessList)
        tempprocessList.remove(min(tempprocessList))
    SJFTime = SJFTime/numProcess
    return SJFTime

def RR(RRTime, temp2processList, numProcess):
    temp = 0
    point = 0
    timeQuantum = (max(temp2processList)+min(temp2processList))//2
    while len(temp2processList) > 0:
        RRTime += temp
        point = point % (len(temp2processList))
        if temp2processList[point] >= timeQuantum:
            temp += timeQuantum
            temp2processList[point] -= timeQuantum
        elif temp2processList[point] < timeQuantum:
            temp += temp2processList[point]
            temp2processList.remove(temp2processList[point])
            point -= 1
        point += 1
    RRTime = RRTime/numProcess
    return RRTime

#################### main ################################
# Workbook is created 
wb = Workbook() 
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 

while command != "Y" and command != "N" :
    command = input("Process with Arrival Time (Y/N) : ")
    command = command.upper()

case = int(input("Enter number of case : "))
WriteHeaderSheet(command, case)

for x in range(case):
    p1 = 0
    p2 = 0
    p3 = 0
    processList.clear()
    sumTime = 0
    temp = generateListData(p1, p2, p3, processList, sumTime)
    numProcess = temp[0][0] + temp[0][1] + temp[0][2]
###FCFS
    FCFSTime = 0
    FCFSTime = FCFS(FCFSTime, processList, numProcess)
###SJF
    tempprocessList = processList.copy()
    SJFTime = 0
    SJFTime = SJF(SJFTime, tempprocessList, numProcess)
###RR
    temp2processList = processList.copy()
    RRTime = 0
    RRTime = RR(RRTime, temp2processList, numProcess)
###
    WriteDataSheet(x, temp[0][0], temp[0][1], temp[0][2], FCFSTime, SJFTime, RRTime, temp[1], temp[2])
    
wb.save('cpu_time_scheduling.xls') 