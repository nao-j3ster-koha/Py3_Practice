a,b = map(int, input().split())
while ( a < 1 or a > 9999 ) or ( b < 1 or b > 9999):
    a,b = map(int, input().split())

if ( a*b > 9999):
    rslt = 'NG'
else:
    rslt = a*b

print(rslt)
