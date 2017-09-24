m,n = map(int, input().split())

while( m < 1 or m > 20 ) or ( n < 1 or n > 20):
    m,n = map(int, input().split())

if ( n >= m ):
    rslt = n - m
else:
    rslt = 'No'

print(rslt)
