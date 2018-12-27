m,n = map(int, input().split())

dtlist = []

for i in range(m):
    tmplist = []
    d, r = map(int, input().split())
    tmplist.append(d)
    tmplist.append(r)
    dtlist.append(tmplist)


dic_rainrate = {}
for j in range(0, len(dtlist) - ( n -1 ) ):
    startdate = dtlist[j][0]
    tmpRainrate = 0
    diclabel = str(startdate)
    dic_rainrate.setdefault(diclabel,0)

    for k in range(n):
        tmpRainrate += dtlist[j + k][1]
    dic_rainrate[diclabel] = tmpRainrate

min_key = min(dic_rainrate, key=dic_rainrate.get)
last_day = int(min_key) + ( n -1 )
result = str(min_key) + ' ' + str(last_day)
print(result)



