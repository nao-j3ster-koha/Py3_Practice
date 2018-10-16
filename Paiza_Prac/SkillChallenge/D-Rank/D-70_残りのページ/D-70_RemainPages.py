m,n = map(int, input().split())
while ( m < 1 or m > 100) \
    or ( n < 1 or n > 100) \
    or ( n > m):
    m,n = manp(int, input().split())


print(m-n)
