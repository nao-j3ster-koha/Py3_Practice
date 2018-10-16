srcStr1 = input()
while ( len(srcStr1) < 1 or len(srcStr1) > 100 ):
    srcStr1 = input()

dstStr1 = ''
for i in range(len(srcStr1)-1,-1,-1):
    dstStr1 = dstStr1 + srcStr1[i]
print(dstStr1)
