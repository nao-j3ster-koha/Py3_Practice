import re

str1 = input()

while( int(len(str1)) < 1 or int(len(str1)) > 100 ):
    str1 = input()

str1.lower()

str2 = str1.replace('at', '@')

print(str2)


