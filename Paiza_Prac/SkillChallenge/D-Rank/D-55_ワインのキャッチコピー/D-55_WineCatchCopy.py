str1,str2 = map(str, input().split())

while( len(str1) < 1 or len(str1) > 20 ) or ( len(str2) < 1 or len(str2) > 20 ):
    s1,s2 = map(str, input().split())

print('Best in {0} {1}'.format(str1, str2))
