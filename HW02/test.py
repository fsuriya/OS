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

    return pageFaults

dataList = [1,2,3,4,1,2,5,1,2,3,4,5]
dataList2 = [7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
print(Optimal(dataList2, 3))
# print(dataList.index(max(dataList)))