N = int(input())

while ( N < 2 or N > 100):
    N = int(input())

ans = int((N * ( N -1 ))/2)

print(ans)
