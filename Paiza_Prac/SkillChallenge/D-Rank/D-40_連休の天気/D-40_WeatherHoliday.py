srcList = []

for i in range(7):
    num = int(input())
    while( num < 0 or num > 100):
        num = int(input())
    srcList.append(num)

cnt = 0
for m in range(len(srcList)):
    if( int(srcList[m]) <= 30 ):
        cnt += 1

print(cnt)
