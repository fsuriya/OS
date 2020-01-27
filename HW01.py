################### Global variable ######################
numOfProcess = 0        #Number of Process
p1 = 0                  #percent of process time 2-8   ms
p2 = 0                  #percent of process time 20-30 ms
p3 = 0                  #percent of process time 35-40 ms
command = ""

################### Function #############################
def genProcessList(command, numOfProcess, p1, p2, p3):
    print(command, numOfProcess, p1, p2, p3)

    textFile = open("example.txt", "w")
    textFile.write("Process with Arrival Time : ")
    textFile.write(command % "\n")
    textFile.close()

#################### main ################################
while command != "Y" and command != "N" :
    command = input("Process with Arrival Time (Y/N) : ")
    command = command.upper()

numOfProcess = int(input("Enter number of process : "))

while p1+p2+p3 != 100 :
    p1 = float(input("Enter percent of process time 2-8   ms : "))
    p2 = float(input("Enter percent of process time 20-30 ms : "))
    p3 = float(input("Enter percent of process time 35-40 ms : "))
    if p1+p2+p3 > 100:
        print("total percent over 100\n")

genProcessList(command, numOfProcess, p1, p2, p3)