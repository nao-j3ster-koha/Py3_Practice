numStr = input()

rslt = 0

for i in range(1,len(numStr)):
    if numStr[i] == numStr[0]:
        rslt += 1
if rslt == len(numStr) - 1 :
    print(numStr)
else:
    print('No')
