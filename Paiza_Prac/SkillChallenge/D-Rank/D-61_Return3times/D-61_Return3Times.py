chc = int(input())
while ( chc < 0 or chc > 100):
    chc = int(input())


if( chc == 0 ):
    rslt = 1
else:
    rslt = chc * 3

print(rslt)
