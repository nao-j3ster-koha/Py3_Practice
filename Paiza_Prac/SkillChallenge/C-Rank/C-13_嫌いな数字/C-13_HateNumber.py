hateNum = int(input())
while ( hateNum < 0 or hateNum > 9):
    hateNum = int(input())

roomSum = int(input())
while ( roomSum < 1 or roomSum > 100):
    roomNum = int(input())
rsltNum = []
failCount = 0
for i in range(roomSum):
    roomNum = input()
    while ( int(roomNum) < 1 or int(roomNum) > 1000):
        roomNum = input()
    if ( roomNum.count(str(hateNum)) == 0):
        rsltNum.append(roomNum)
    else:
        failCount += 1
if ( failCount == roomSum):
    print('none')
else:
    for n in range(len(rsltNum)):
        print(rsltNum[n])



