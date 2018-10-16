import re

str = input()

while ( int(len(str)) < 1 or int(len(str)) > 100):
    str = input()

#rslt = str.replace('False','True')
#print(rslt)
print(str.replace('False','True'))

