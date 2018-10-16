turnNum, initHP, thlsHP, rcvrHP = map(int, input().split())

while ( turnNum < 1 or turnNum > 100 ) \
        or ( initHP < 1 or initHP > 20000) \
        or ( thlsHP < 1 or thlsHP > 9999 ) \
        or ( rcvrHP < 1 or rcvrHP > 10000) \
        or ( thlsHP > initHP and thlsHP > rcvrHP ):
    turnNum, initHP, thlsHP, rcvrHP = map(int, input().split())


#print(dmgNum)
chkDmg = 0

while( chkDmg != turnNum):
    dmgNum = input().split()
    chkDmg = 0
    for i in range(turnNum):
        if ( int(dmgNum[i]) >= -10000 and  int(dmgNum[i]) <= 10000 ) and ( int(dmgNum[i]) != 0):
            chkDmg += 1

#for i, dmg in enumerate(dmgNum):
for i in range(len(dmgNum)):
    if ( initHP + int(dmgNum[i]) < 0):
        print(initHP)
        exit()
    else:
        initHP += int(dmgNum[i])
        if ( int(dmgNum[i]) < 0 and initHP <= thlsHP):
            initHP += rcvrHP

print(initHP)