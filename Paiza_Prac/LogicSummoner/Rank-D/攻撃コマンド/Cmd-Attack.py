cmdList = []
for i in range(5):
    cmdStr = input()
    while( cmdStr != 'Attack' and cmdStr != 'Defense'):
        cmdStr = input()
    cmdList.append(cmdStr)

sumDamage = 0

for i,cmd in enumerate(cmdList):
    if( cmd == 'Attack'):
        sumDamage += 100
    else:
        sumDamage += 0

print(sumDamage)

