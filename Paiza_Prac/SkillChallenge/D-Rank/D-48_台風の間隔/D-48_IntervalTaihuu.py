
    dtlist = []
    for i in range(0,5,1):
        dt = int(input())
        while  ( dt < 1 or dt > 31):
            dt = int(input())
        dtlist.append(dt)
        i += 1

    for n in range(len(dtlist)-1):
        k = n+1
        if( dtlist[k-1] > dtlist[k]):
            w = dtlist[k]
            dtlist[k-1] = dtlist[k]
            dtlist[k-1] = w


    for m in range(len(dtlist)-1):
        rslt = dtlist[m+1] - dtlist[m]
        print(str(rslt))


