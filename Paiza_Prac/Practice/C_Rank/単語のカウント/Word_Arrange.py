N = input()

while( len(N) < 1 or len(N) > 1000 ):
    N = input()

srcList = N.split()

rsltDict = {}
key_list = []

for k in srcList:
    if k in key_list:
        pass
    else:
        key_list.append(k)

for i in range(len(srcList)):
    chk = srcList[i]
    if ( chk in rsltDict):
        rsltDict[chk] += 1
    else:
        rsltDict[chk] = 1

for key in key_list:
    print(key + ' ' + str(rsltDict[key]))





