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
    sheet1.write(4, 0, "2 - 8 ms")
    sheet1.write(5, 0, "20 - 30 ms")
    sheet1.write(6, 0, "35 - 40 ms")
    sheet1.write(7, 0, "total")
    
    #percent of process
    sheet1.write(9, 0, "percent of process")
    sheet1.write(10, 0, "2 - 8 ms")
    sheet1.write(11, 0, "20 - 30 ms")
    sheet1.write(12, 0, "35 - 40 ms")

    #average waiting time
    sheet1.write(14, 0, "average waiting time")
    sheet1.write(15, 0, "FCFS")
    sheet1.write(16, 0, "SJF")
    sheet1.write(17, 0, "RR")

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
    numProcess = random.randrange(20,61)                   #20 to 60 processes
    p3 = random.randrange(10,21)
    p2 = random.randrange(20,41)
    p3 = (numProcess*p3)//100
    p2 = (numProcess*p2)//100
    p1 = numProcess - (p2+p3)
    for x in range(p1):                                #generate process = numProcess time
        processList.append(random.randrange(2,9))      #process time 2 to 8 ms
    for x in range(p2):
        processList.append(random.randrange(20,31))    #process time 20 to 30 ms
    for x in range(p3):
        processList.append(random.randrange(35,41))    #process time 35 to 40 ms
    for x in range(numProcess):
        sumTime += processList[x]    
    random.shuffle(processList)

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
    countTime = 0
    endProcess = [0] * numProcess
    timeQuantum = 8
    point = 0
    while len(temp2processList) > 0:
        point = point % (len(temp2processList))
        RRTime += (countTime - endProcess[point])
        if temp2processList[point] > timeQuantum:
            temp2processList[point] -= timeQuantum
            countTime += timeQuantum
            endProcess[point] = countTime
        elif temp2processList[point] <= timeQuantum:
            countTime += temp2processList[point]
            temp2processList.remove(temp2processList[point])
            endProcess.remove(endProcess[point])
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