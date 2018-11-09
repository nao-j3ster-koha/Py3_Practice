tgtStr = input()

numSample = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
rsltNumChar = ''

for i in range(len(tgtStr)):
    if tgtStr[i] in numSample:
        rsltNumChar += tgtStr[i]

print(rsltNumChar)
