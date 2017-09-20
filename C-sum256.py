def check_Aklist(name='AkList'):
#    chkAK = 0
    for i in range(len(name)):
        if( int(name[i]) >= 0 and int(name[i]) <= 256):
            chkAK += 1
    print(str(chkAK))
    return chkAK


AkList = []
chkAK = 0

N = int(input())

while ( N < 2 or N > 100):
    N = int(input())

AkList = input().split()
print(AkList)
#check_Aklist

for i in range(len(AkList)):
    if (int(AkList[i]) >= 0 and int(AkList[i]) <= 256):
        chkAK += 1

while (chkAK != N):
    AkList = input().split()
    check_Aklist

print(str(chkAK))




