c1 , c2 = map(str, input().split())

while( c1 != 'J' and c1 != 'Q' and c1 != 'K') or ( c2 != 'J' and c2 != 'Q' and c2 != 'K' ):
    c1 , c2 = map(str, input().split())

if ( c1 == 'J' and c2 =='J'):
    c2 = 'Q'

print('{0} {1}'.format(c1, c2))
