N = int(input())
while ( N < 1 or N > 1000):
    N = int(input())
pointCnt = 0
for i in range(N):
    d1,d2 = map(int, input().split())
    while ( d1 < 1 or d1 > 31) or ( d2 < 1 or d2 > 10000):
        d1, d2 = map(int, input().split())
    if ( d1  == 3 ) or ( d1 == 13 ) or ( d1 == 23 ) or ( d1 == 30) or ( d1 == 31):
        pointPct = 0.03
        pointCnt += int(d2 * pointPct)
    elif ( d1 == 5 ) or ( d1 == 15 ) or ( d1 == 25 ):
        pointPct = 0.05
        pointCnt += int(d2 * pointPct)
    else:
        pointCnt += int(d2 * 0.01)
rslt = int(pointCnt)
print(rslt)


