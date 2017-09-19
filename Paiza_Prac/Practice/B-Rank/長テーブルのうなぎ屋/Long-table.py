# パラメータデータの入力
# グループの数と、
tblLength, grpNum = map(int, input().split())
while ( tblLength < 1 or tblLength > 100) or (grpNum < 1 or grpNum > 100):
    tblLength, grpNum = map(int, input().split())

srcList = []

for i in range(grpNum):
    prsnNum, chairPos =map(int, input().split())
    srcList.append([prsnNum, chairPos])

sitNum = 0
tblStatus = []
for i in range(tblLength):
    tblStatus.append(0)


customerNum = 0

for k in range(grpNum):
    prsnNum = srcList[k][0]
    chairPos = srcList[k][1]
    sitStatus = 0
    for m in range(chairPos-1,chairPos-1+prsnNum,1):
        if ( tblStatus[m] == 0):
            sitStatus += 1
            tblStatus[m] = 1
#            print(tblStatus)
    if ( prsnNum == sitStatus):
        customerNum += prsnNum
#        print(str(customerNum))

print(str(customerNum))
