otherList = []
otherList = input().split()

for i in range(len(otherList)):
    while( int(otherList[i]) < 0 or int(otherList[i]) > 59):
        otherList = map(int, input().split())


for n in range(len(otherList)):
    m = n + 1
    for m in range(len(otherList)-1):
        if( int(otherList[m]) > int(otherList[m+1])):
            w = otherList[m+1]
            otherList[m+1] = otherList[m]
            otherList[m] = w

a = int(input())

while( a < 0 or a > 59):
    a = int(input())

cntNG = 0

for j in range(len(otherList)):
    if( int(otherList[j]) < int(a) ):
        cntNG += 1

print(cntNG+1)







