
srcStrings = input()

while((len(srcStrings) < 1 or len(srcStrings) > 100) or (srcStrings.count('b') + srcStrings.count('w') != len(srcStrings)  )):
    srcStrings = input()

cntWhite = srcStrings.count('w')
cntBlack = srcStrings.count('b')

srcStrings_list = []
for m in srcStrings:
    srcStrings_list.append(m)

if( srcStrings_list[0] == 'w'):
    print("0 " + str(cntWhite) + ' ' + str(cntBlack))
else:
    print(str(cntBlack) + ' ' + str(cntWhite))




