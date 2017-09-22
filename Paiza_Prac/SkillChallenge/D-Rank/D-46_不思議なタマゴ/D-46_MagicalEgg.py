
d_1,d_2,d_3 = map(int, input().split())

while ( d_1 < 1 or d_1 > 100) or ( d_2 < 1 or d_2 > 100 ) or ( d_3 < 1 or d_3 > 100):
    d_1,d_2,d_3 = map(int, input().split())

srcList = []
srcList.append(d_1)
srcList.append(d_2)
srcList.append(d_3)

for m in range(len(srcList)-1):
    n = m + 1
    if ( srcList[n-1] > srcList[n]):
        w = srcList[n]
        srcList[n] = srcList[n-1]
        srcList[n-1] = w

print(str(srcList[2]))




