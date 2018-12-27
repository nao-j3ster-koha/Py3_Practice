H, W = map(int, input().split())

resultList = []

for i in range(H):
    scaleList = []
    scaleList = input().split()
    for j in range(len(scaleList)):
        if int(scaleList[j]) >= 128:
            scaleList[j] = 1
        else:
            scaleList[j] = 0
    resultList.append(scaleList)

for i in range(H):
    rsltStr = ''
    for k in range(W):
        rsltStr += str(resultList[i][k]) + ' '
        rslt = rsltStr.rstrip()
    print(rslt)

