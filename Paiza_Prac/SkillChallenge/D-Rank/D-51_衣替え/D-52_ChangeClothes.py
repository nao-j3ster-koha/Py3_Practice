
strList = input().split()

while( int(len(strList)) < 1 or int(len(strList)) > 10) or ( strList.count('W') + strList.count('S') != int(len(strList))):
    strList = input().split()


if( strList.count('W') >= 5):
    rslt = 'OK'
else:
    rslt = 'NG'

print(rslt)





