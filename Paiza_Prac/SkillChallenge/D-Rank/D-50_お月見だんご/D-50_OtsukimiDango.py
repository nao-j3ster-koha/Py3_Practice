d1,d2 = map(int, input().split())

while ( d1 < 1 or d1 > 1000) or ( d2 < 1 or d2 > 1000):
    d1,d2 = map(int, input().split())

if ( d1 > 5):
    d1 = 5

if (d2 > 5):
    d2 = 5

print(str(d1 + d2))





