a = int(input())
b = int(input())
c = int(input())

while ( a < 1 or a > 100):
    a = int(input())

while ( b < 1 or b > 100):
    b = int(input())

while (c < 1 or c > 100):
    c = int(input())

if( a == b == c):
    rslt = 'OK'
else:
    rslt = 'NG'
print(rslt)


