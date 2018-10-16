s1, s2 = map(str, input().split())

while ( int(len(s1) < 1 or int(len(s1)) > 100)) or ( s2 != 'M' and s2 != 'F'):
    s1, s2 = map(str, input().split())

if ( s2 == 'M'):
    grtStr = 'Hi, Mr. '
elif( s2 == 'F'):
    grtStr = 'Hi, Ms. '

print( grtStr + s1)

