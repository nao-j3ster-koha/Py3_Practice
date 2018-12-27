N = int(input())

compTable = []

for i in range(N + 1):
    tmpList = []
    tmpList = input().split()
    compTable.append(tmpList)

print(compTable)

stdPlace = compTable[-1][0]
stdHour = int(compTable[-1][1].split(':')[0])
stdMin = compTable[-1][1].split(':')[1]

print(stdPlace)
print(str(stdHour))
print(str(stdMin))

for i in range(N):
    if compTable[i][0] == stdPlace:
        stdTimediff = int(compTable[i][1])

for i in range(N):
    diffHour = int(compTable[i][1]) - stdTimediff
    tgtHour =  stdHour + diffHour
    if tgtHour <= 0:
        tgtHour += 24
    if tgtHour >= 0 and tgtHour < 10:
        tgtHour = str('0' + str(tgtHour))
    print(str(str(tgtHour) + ':' + str(stdMin)))





