n = int(input())
while ( n < 1 or n > 47):
    n = int(input())

if( n > 24 ):
    rslt = n - 24
else:
    rslt = n

print(rslt)
