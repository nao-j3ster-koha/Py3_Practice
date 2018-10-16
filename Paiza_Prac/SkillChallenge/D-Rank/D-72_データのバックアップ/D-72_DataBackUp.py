x,y,p = map(int,input().split())
while ( x < 1 or x > 1000 ) \
    or ( y < 1 or y > 1000) \
    or ( p < 1 or p > 10000):
    x,y,p = map(int,input().split())

if ( x % y != 0):
    qty = int(( x / y )) + 1
    price = p * qty
    print(price)
else:
    qty = int(x / y)
    price = p * qty
    print(price)
