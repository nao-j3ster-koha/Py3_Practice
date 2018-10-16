
list = []

for i in range(1,11):
    num = int(input())
    while(num < 0 or num > 100):
        print("正しい範囲の数値を入力してください")
        num=int(input())

    list.append(str(num))

print(list)

for n in range(0,len(list)):
    w = ''
    t = ''
    j = n + 1
    print("ループ"+str(n)+"回目："+ str(list))
    for j in range(n,len(list)):
        if(int(list[j]) < int(list[n])):
            w = list[j]
            t = list[n]
            list[n]=w
            list[j]=t
        j += 1
    n += 1

print(list)
data_str = ",".join(list)

print(data_str)


