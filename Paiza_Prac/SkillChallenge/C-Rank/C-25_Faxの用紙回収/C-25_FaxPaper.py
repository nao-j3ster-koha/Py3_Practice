cap = int(input())

n = int(input())

rndCount = 0
hrNum = 0
hrPaperCount = 0

for i in range(n):
    tmpList = list(map(int, input().split()))
    if i == 0:
        hrNum = tmpList[0]
        hrPaperCount = tmpList[2]
    elif i != n-1:
        if hrNum == tmpList[0]:
            hrPaperCount += tmpList[2]
        elif hrNum != tmpList[0]:
            hrNum = tmpList[0]
            if int(hrPaperCount % cap) == 0:
                rndCount += int(hrPaperCount / cap )
            else: rndCount += int(hrPaperCount / cap ) + 1
            hrPaperCount = tmpList[2]
    elif i == n-1:
        hrPaperCount += tmpList[2]
        if int(hrPaperCount % cap) == 0:
            rndCount += int(hrPaperCount / cap )
        else: rndCount += int(hrPaperCount / cap ) + 1
print(rndCount)