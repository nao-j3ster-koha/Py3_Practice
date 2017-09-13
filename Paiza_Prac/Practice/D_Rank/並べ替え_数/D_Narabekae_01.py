def get_input():
    while True:
        try:
            dl = input()
            if (dl == ''):
                break
            while(int(dl) < 0 or int(dl) > 100):
                dl = input()
            yield ''.join(dl)
        except EOFError:
            break

if __name__ == '__main__':
    src_data = list(get_input())

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
data_str = ",".join(src_data)
print(data_str)


