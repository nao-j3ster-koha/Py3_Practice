N,M,K = map(int, input().split())
while( N < 1 or N > 100) \
    or ( M < 1 or M > 1000) \
    or ( K < 1 or K > M):
    N,M,K = map(int, input().split())

CiList = input().split()
chkCi = 0
while(chkCi != len(CiList)):
    for i in range(N):
        while ( float(CiList[i]) < 0 or float(CiList[i]) > 100) \
                or ( len(CiList) !=  N):
            CiList = input().split()
        chkCi += 1

XsumList =[]

for m in range(M):
    XiList = input().split()
#    while( len(XiList) != N):
#        XiList = input().split()
    chkXi = 0
    while( chkXi != len(XiList)):
        for i in range(len(XiList)):
            while( int(XiList[i]) < 1 or int(XiList[i]) > 100000 ):
                XiList = input().split()
            chkXi += 1

    Xsum = 0
    for x in range(N):
        Xsum += float(CiList[x]) * int(XiList[x])
    Xsum = int(round(Xsum))

    XsumList.append(int(Xsum))

for j in range(len(XsumList)):
    l = j + 1
    for l in range(len(XsumList)-1):
        if(XsumList[l] > XsumList[l+1]):
            w = XsumList[l]
            XsumList[l] = XsumList[l+1]
            XsumList[l+1] = w

for k in range(M-1,M-K-1,-1):
    print(XsumList[k])
