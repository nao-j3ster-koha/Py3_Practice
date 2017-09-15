
srcStrings = input()

while((len(srcStrings) < 1 or len(srcStrings) > 100) and (srcStrings.count('b') + srcStrings.count('w') < 1 or srcStrings.count('b') + srcStrings.count('w') >100 )):
    srcStrings = input()

cntWhite = srcStrings.count('w')
cntBlack = srcStrings.count('b')

srcStrings_list = []
for m in srcStrings:
    srcStrings_list.append(m)

if( srcStrings_list[0] == 'w'):
    print("0 "+ str(cntWhite) + ' ' + str(cntBlack) + '\n')
else:
    print(str(cntBlack) + ' ' + str(cntWhite) + '\n')




