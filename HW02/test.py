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
        
        print(frameList)

    return pageFaults

def Optimal (dataList, frame):
    pageFaults = 0
    frameList = [-1] * frame
    countOlder = [0] * frame

    for i in range(len(dataList)):
        print(i)
        if(frameList.count(-1) != 0):
            point = frameList.index(-1)
        else:
            point = countOlder.index(max(countOlder))

        if(frameList.count(dataList[i]) == 0):
            pageFaults += 1
            frameList[point] = dataList[i]
            countOlder[point] = 0
        else: 
            countOlder[frameList.index(dataList[i])] = 0
        #update countOlder
        for j in range(frame):
            if frameList[j] != -1:
                countOlder[j] += 1
        print(frameList)
        print(countOlder)

    return pageFaults

dataList = [1,2,3,4,1,2,5,1,2,3,4,5]
#dataList = [1,2,3,4,1,2,5,2]
print(Optimal(dataList, 4))
#print(dataList.index(-1))