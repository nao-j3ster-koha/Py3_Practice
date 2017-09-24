L,M,N = map(int, input().split())
while ( L < 1 or L > 20) or ( M < 1 or M > 20) or ( N < 1 or N > 20):
    L,M,N = map(int, input().split())

print( 'A'*L + 'B'*M + 'A'*N)
