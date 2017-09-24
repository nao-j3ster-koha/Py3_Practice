h1,h2,h3 = map(int,input().split())

while( h1 < 1 or h2 > 10) \
        or (h2 < 1 or h2 > 10) \
        or (h3 < 1 or h3 > 10) \
        or ( h1 + h2 + h3 != 10):
    h1,h2,h3 = map(int,input().split())

ngyList = ['A', 'B','C', 'D', 'E', 'F', 'G', 'H','I', 'J']
str = ''
for i in range(h1):
    str = str + ngyList[i]
print(str)

str = ''
for n in range(h1,h1+h2):
    str = str + ngyList[n]
print(str)

str = ''
for m in range(h1+h2,h1+h2+h3):
    str = str + ngyList[m]
print(str)



