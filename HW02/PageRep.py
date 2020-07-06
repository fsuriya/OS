import random

def FIFO (dataList, frame):
    pageFaults = 0
    frameList = [-1] * frame
    pointFrameList = 0
    for i in range(len(dataList)):
        pointFrameList = pointFrameList % frame
        if(frameList.count(dataList[i]) == 0):
            pageFaults += 1
            frameList[pointFrameList] = dataList[i]
            pointFrameList += 1
        print(str(i)+" : "+str(frameList))

    return pageFaults

def Optimal(dataList, frame):
    pageFaults = 0
    frameList = [-1] * frame
    point = 0
    for i in range(len(dataList)):
        if point < frame:
            frameList[i] = dataList[i]
            pageFaults += 1
            point += 1
        elif frameList.count(dataList[i]) == 0 :
            pageFaults += 1
            checkFar = [1] * frame
            for j in range(i+1, len(dataList)):
                if checkFar.count(1) <= 1:
                    break
                if frameList.count(dataList[j]) != 0:
                    checkFar[frameList.index(dataList[j])] = 0
            frameList[checkFar.index(1)] = dataList[i]
        print(str(i)+" : "+str(frameList))

    return pageFaults

def UpdateOlder(countOlder, frameList):
    for i in range(len(countOlder)):
        if frameList[i] != -1:
            countOlder[i] += 1
    return countOlder

def RLU (dataList, frame):
    pageFaults = 0
    frameList = [-1] * frame
    countOlder = [0] * frame

    for i in range(frame):
        frameList[i] = dataList[i]
        countOlder = UpdateOlder(countOlder, frameList)
        pageFaults += 1
    for j in range(frame, len(dataList)):
        if(frameList.count(dataList[j]) == 0):
            pageFaults += 1
            frameList[countOlder.index(max(countOlder))] = dataList[j]
            countOlder[countOlder.index(max(countOlder))] = 0
        else:
            countOlder[frameList.index(dataList[j])] = 0
        countOlder = UpdateOlder(countOlder, frameList)
        print(str(j)+" : "+str(frameList))

    return pageFaults

data = [0, 1, 2, 4, 0, 1, 0, 5, 1, 1, 2, 4, 5, 0, 2, 1, 4, 0, 2, 5]
# print(len(data))
print(RLU(data,4))