a,b = map(int, input().split())

while ( a < 1 or a > 100 ) or ( b < 1 or b > 100):
    a,b = map(int, input().split())

print(str(a -b))
