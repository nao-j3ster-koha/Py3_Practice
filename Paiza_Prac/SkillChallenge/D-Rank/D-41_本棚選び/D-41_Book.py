n, d, e = map(int, input().split())

while( n < 1 or n > 500) or ( d < 1 or d > 10) or ( e < 1 or e > 500):
    n, d, e = map(int, input().split())


chk = ( d * e) - n

if ( chk > 0 ):
    rslt = 'OK'
else:
    rslt = 'NG'

print(rslt)
