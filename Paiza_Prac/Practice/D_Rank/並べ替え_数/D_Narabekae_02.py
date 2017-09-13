src_data = []

l_num = int(input())

for i in range(l_num):
    dl = input()
    while(int(dl) < 0 or int(dl) > 1000):
        dl = input()
    src_data.append(dl)
    i += 1

for n in range(0,len(src_data)):
    w = ''
    t = ''
    j = n + 1
    for j in range(n, len(src_data)):
        if (int(src_data[j]) < int(src_data[n])):
            w = src_data[j]
            t = src_data[n]
            src_data[n] = w
            src_data[j] = t
        j += 1
    n += 1

for m in range(len(src_data)):
    print(src_data[m])


