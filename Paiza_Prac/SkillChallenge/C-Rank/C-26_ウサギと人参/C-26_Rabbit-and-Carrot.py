N,S,p = map(int,input().split())

rsltList = []

for i in range(N):
    m,s = map(int, input().split())
    if s >= S - p and s <= S + p:
        tmpList = [m, i]
        rsltList.append(tmpList)

rsltList.sort(key=lambda x:[x[0], x[1]])
#rsltList.sort(reverse=True)
#rsltList.sort(key=lambda x:[x[1]])

print(rsltList)
if len(rsltList) > 0:
    print(rsltList[0][1] + 1)
else: print('not found')

