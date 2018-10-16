str = input()

while ( int(len(str)) < 1 or int(len(str)) > 20) or ( str.count('1') != int(len(str))):
    str = input()


if( str.count('1') >= 11):
    rslt = 'OK'
else:
    rslt = 11 - int(len(str))

print(rslt)

