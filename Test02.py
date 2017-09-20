y,m,d = map(str, input().split())

while( int(y) < 2000 or int(y) > 2016) or ( int(m) < 1 or int(m) > 12 ) or ( int(d) < 1 or int(d) > 31):
    y,m,d = map(str, input().split())

print(y + '/'+m + '/' + d)
