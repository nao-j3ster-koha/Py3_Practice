n = int(input())

while ( n < 1 or n > 100):
    n = int(input())

if ( n % 2 == 0 ):
    rslt = 'OFF'
else:
    rslt = 'ON'

print(rslt)
