n1,n2 = map(int, input().split())

while ( n1 < -1000 or n1 > 1000) or (n2 < -1000 or n2 > 1000):
    n1,n2 = map(int, input().split())

n3, n4 = map(int, input().split())
while ( n3 < -1000 or n3 > 1000) or (n4 < -1000 or n4 > 1000):
    n3,n4 = map(int, input().split())


ans = (n1 * n4) - (n2 * n3)
print(ans)


