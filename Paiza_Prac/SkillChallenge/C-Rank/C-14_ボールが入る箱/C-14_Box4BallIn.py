n,r = map(int, input().split())
while ( n< 1 or n > 100 ) or ( r < 1 or r > 100):
    n, r = map(int, input().split())

rsltList = []

for i in range(n):
    h, w, d = input().split()
    while ( int(h) < 1 or int(h) > 200 ) or ( int(w) < 1 or int(w) > 200 ) or ( int(d) < 1 or int(d) > 200):
        h, w, d = input().split()

    if (  int(h) - (r * 2) >= 0 ) and ( int(w) - (r * 2) >= 0 ) and ( int(d) - (r * 2)>= 0):
        rslt = i + 1
        rsltList.append(str(rslt))

for m in range(len(rsltList)):
    print(rsltList[m])
