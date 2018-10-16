A1,A2 = map(int, input().split())
while ( A1 < 1 or A1 > 10 ) or ( A2 < 1 or A2 > 4):
    A1, A2 = map(int, input().split())

n = int(input())
while ( n < 1 or n > 40):
    n = int(input())

childCardList = []
for i in range(n):
    B1,B2 = map(int, input().split())
    while( B1 < 1 or B1 > 10 ) or ( B2 < 1 or B2 >4):
        B1, B2 = map(int, input().split())
    childCardList.append([B1,B2])

for i in range(n):
    if ( A1 > childCardList[i][0]):
        rslt='High'
    elif( A1 < childCardList[i][0]):
        rslt = 'Low'
    elif( A1 == childCardList[i][0]):
        if( A2 < childCardList[i][1]):
            rslt = 'High'
        elif( A2 > childCardList[i][1]):
            rslt = 'Low'
    print(rslt)
