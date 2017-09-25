t, m = map(int, input().split())
while ( t < 0 or t > 40) \
    or ( m < 0 or m > 100):
    t, m = map(int, input().split())

if ( t >= 25 and m <= 40):
    rslt = 'No'
elif( t >= 25 or m <= 40 ):
    rslt = 'Yes'
else:
    rslt = 'No'

print(rslt)



