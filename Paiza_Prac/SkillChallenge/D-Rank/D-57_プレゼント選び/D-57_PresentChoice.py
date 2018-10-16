num = int(input())
while( num < 1 or num > 3):
    num = int(input())

PresentList = []
chkLng = 0

while( chkLng != 3):
    chkLng = 0
    str1,str2,str3 = map(str,input().split())
    PresentList.append(str1)
    PresentList.append(str2)
    PresentList.append(str3)
    for m in range(3):
        if ( len(PresentList[m]) >= 1 and len(PresentList[m]) <= 20):
            chkLng += 1

print(PresentList[num-1])


