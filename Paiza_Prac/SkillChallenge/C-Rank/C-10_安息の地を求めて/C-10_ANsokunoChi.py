a,b,R = map(int,input().split())
while ( a < 0 or a > 100) or ( b < 0 or b > 100) or( R < 1 or R > 100 ):
    a, b, R = map(int, input().split)

N = int(input())
while ( N < 1 or N > 1000):
    N = int(input())
rsltList = []
for i in range(N):

    x, y = input().split()
    while ( int(x) < 0 or int(x) > 100) or ( int(y) < 0 or int(y) > 100):
        x,y = input().split()
    if ( (int(x) - a )**2 + ( int(y) - b )**2 >= R ** 2):
        readPos = 'silent'
    else:
        readPos = 'noisy'
    rsltList.append(readPos)

for i in range(N):
    print(rsltList[i])


