n = int(input())

rcpList =[]
for i in range(n):
    a1,b1 = map(str, input().split())
    rcpList.append([a1,b1])

m = int(input())

matDict = {}
if ( m > 0):
    for j in range(m):
        c1,d1 =map(str, input().split())
        matDict[c1] = d1

    rsltList = []
    for k in range(n):
        if ( rcpList[k][0] in matDict):
            if(int(matDict[str(rcpList[k][0])]) > 0):
                t = int(int(matDict[str(rcpList[k][0])]) / int(rcpList[k][1]))
        else:
            t = 0
        rsltList.append(t)
    rsltList.sort()
    print(rsltList[0])
else:
    rslt = 0
    print(rslt)



