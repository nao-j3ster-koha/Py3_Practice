xc,yc,r1,r2 = map(int,input().split())

n = int(input())
rsltList =[]

for i in range(n):
    xt,yt = map(int,input().split())

    tmpR = ( (xt -xc ) **2) + ( (yt - yc) ** 2)
    if ( r1 **2 <= tmpR ) and ( r2 **2 >= tmpR):
        rsltList.append('yes')
    else: rsltList.append('no')

for item in rsltList:
    print(item)
