import re

str = input()
while(int(len(str)) < 1 or int(len(str)) > 20 ) or (str.count('noaki') > 1 ):
    str = input()

rslt = str.replace('noaki','')

print(rslt)