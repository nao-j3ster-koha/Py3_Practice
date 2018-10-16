m,p,q = map(int,input().split())

rslt1 = m - ( m * ( p /100))
rslt2 = rslt1 - rslt1 * ( q /100)

print(rslt2)
