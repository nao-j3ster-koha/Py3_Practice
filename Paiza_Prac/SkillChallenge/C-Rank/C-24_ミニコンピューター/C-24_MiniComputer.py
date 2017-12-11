n = int(input())

a1 = 0
a2 = 0

for i in range(n):
    tmpList = list(map(str, input().split()))
    if tmpList[0] == 'SET' and tmpList[1] == '1':
        a1 = int(tmpList[2])
    elif tmpList[0] =='SET' and tmpList[1] =='2':
        a2 = int(tmpList[2])
    elif tmpList[0] == 'ADD':
        a2 = a1 + int(tmpList[1])
    elif tmpList[0] == 'SUB':
        a2 = a1 - int(tmpList[1])

print(str(a1) + ' ' + str(a2))
