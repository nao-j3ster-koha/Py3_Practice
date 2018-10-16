scr = 0
scrSum = 0
scrList = []

scrList = input().split()
print(scrList)


for i in range(7):
    scrSum += int(scrList[i])

scrAvg = round(float(scrSum / 7),1)

print(scrAvg)
