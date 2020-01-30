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

FCFSTime = 0
processList = [5,4,3,2,1]
tempprocessList = processList.copy()
temp2processList = processList.copy()
num = 5
print(FCFS(FCFSTime, processList, num))
print(SJF(FCFSTime, tempprocessList, num))
print(RR(FCFSTime, temp2processList, num))