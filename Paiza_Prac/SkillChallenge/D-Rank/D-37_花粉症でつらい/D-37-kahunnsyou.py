M = int(input())

while ( M < 1 or M > 100):
    M = int(input())

N = int(input())
while ( N < 1 or N > 100):
    N = int(input())

ans = int(N / M)
chk = N % M

if( chk == 0):
    rslt = ans
else:
    rslt = ans + 1

print(str(rslt))



