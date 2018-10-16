scrList = []

scrList=input().split()

X = int(input())

totalScr=0
for i in range(len(scrList)):
    totalScr+=int(scrList[i])

avgScr = int(totalScr / 7)

if avgScr >= X:
    rslt= 'pass'
else:
    rslt = 'failure'

print(rslt)
