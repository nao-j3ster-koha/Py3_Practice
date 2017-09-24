num = input()
while( int(num) < 100 or int(num) > 999):
    num = int(input())


if( int(num) >= 200 and int(num) <= 299 ):
    rslt = 'ok'
elif( int(num) >= 400 and int(num) <= 499 ):
    rslt = 'error'
else:
    rslt = 'unknown'

print(rslt)
