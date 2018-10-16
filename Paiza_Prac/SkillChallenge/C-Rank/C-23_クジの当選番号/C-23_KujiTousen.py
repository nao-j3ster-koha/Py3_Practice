tousenList = list(map(int, input().split()))

n = int(input())
rsltList = []
for i in range(n):
    rsltCount = 0
    tmpList = list(map(int, input().split()))
    for t in range(len(tousenList)):
        if tousenList[t] in tmpList:
            rsltCount += 1
    rsltList.append(rsltCount)

for i in rsltList:
    print(i)

