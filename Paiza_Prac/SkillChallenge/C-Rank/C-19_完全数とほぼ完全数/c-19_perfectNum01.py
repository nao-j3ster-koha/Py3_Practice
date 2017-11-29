Q = int(input())

srcList = []
rsltList =[]
for i in range(Q):
    divList = []
    src = int(input())
    for t in range(1,src+1):
        if src % t == 0:
            divList.append(t)

    tmpSum = 0
    for s in range(len(divList)-1):
        tmpSum += divList[s]

    if tmpSum - src == 0:
        rslt = 'perfect'
    elif abs(tmpSum - src) == 1:
        rslt = 'nearly'
    else: rslt = 'neither'

    rsltList.append(rslt)

for i in rsltList:
    print(i)



