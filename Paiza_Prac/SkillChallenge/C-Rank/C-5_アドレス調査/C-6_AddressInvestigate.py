import re
# IPアドレスの数を入力（1 <= M <= 100)
M = int(input())
while ( M < 1 or M > 100):
    M = int(input())

addList = []
for i in range(M):
    addStr = input()
    while ( int(len(addStr)) < 1 or int(len(addStr)) > 100 ) \
            or ( (len(re.findall('\d', addStr)) + addStr.count('.') ) != len(addStr) ):
        addStr = input()
    addList.append(addStr)


for idx, addChar in enumerate(addList):
    tmpList = addChar.split('.')
    if ( len(tmpList) != 4 ) or ( ('' in tmpList) == True):
        rslt = 'False'
    else:
        addChekrslt = 0
        for j in range(len(tmpList)):
            if( int(tmpList[j]) >= 0 and int(tmpList[j]) <= 255 ):
                addChekrslt += 1
        if ( addChekrslt == int(len(tmpList))):
            rslt = 'True'
        else:
            rslt = 'False'
    print(rslt)





