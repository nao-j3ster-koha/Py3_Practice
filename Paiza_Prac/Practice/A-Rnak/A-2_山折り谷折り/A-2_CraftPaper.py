num = int(input())

while(num < 1 or num > 20):
    num = int(input())

rslt = ''

lChr='0'
tChr='1'

for i in range(1,num+1):
    rslt = lChr * num + tChr * (num - 1)

print(rslt)






