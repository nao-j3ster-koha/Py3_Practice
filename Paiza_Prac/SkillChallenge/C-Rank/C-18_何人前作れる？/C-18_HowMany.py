n = int(input())
#while ( n < 1 or n > 100):
#    n = int(input())

rcpList =[]

for i in range(n):
    a1,b1 = map(str, input().split())
#    while( len(a1) < 1 or len(a1) > 10) or ( int(b1) < 1 or int(b1) > 100):
#        a1,b1 = map(str, input().split())
    rcpList.append([a1,b1])

m = int(input())
#while ( m < 0 or m > 100):
#    m = int(input())


matDict = {}
if ( m > 0):
    for j in range(m):
        c1,d1 =map(str, input().split())
#    while( len(c1) < 1 or len(c1) > 10) or ( int(d1) < 1 or int(d1) > 10000):
#        c1,d1 =map(str, input().split())
        matDict[c1] = d1

    rsltList = []
    for k in range(n):
        if ( rcpList[k][0] in matDict):
            if(int(matDict[str(rcpList[k][0])]) > 0):
                t = int(int(matDict[str(rcpList[k][0])]) / int(rcpList[k][1]))
        else:
            t = 0
        rsltList.append(t)

    for p in range(len(rsltList)-1):
        q = n - (p + 1)
        for q in range(q,0,-1):
            if(rsltList[q-1] > rsltList[q]):
                w = rsltList[q-1]
                rsltList[q-1] = rsltList[q]
                rsltList[q] = w
    print(rsltList[0])
else:
    rslt = 0
    print(rslt)



