n = int(input())

while ( n < 0 or n > 100):
    n = int(input())


if ( n >=0 and n <= 30):
    rslt = 'sunny'
elif( n > 30 and n <= 70 ):
    rslt = 'cloudy'
elif( n > 70 ):
    rslt = 'rainy'

print(rslt)