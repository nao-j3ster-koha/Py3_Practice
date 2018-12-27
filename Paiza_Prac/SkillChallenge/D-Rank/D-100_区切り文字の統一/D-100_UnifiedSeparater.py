import re
str = input()

cntH = 0
cntU = 0

for chr in str:
    if chr == '-':
        cntH += 1
    elif chr == '_':
        cntU += 1

if cntH >= cntU:
    dst = str.replace('_', '-')
elif cntU > cntH:
    dst = str.replace('-', '_')

print(dst)
