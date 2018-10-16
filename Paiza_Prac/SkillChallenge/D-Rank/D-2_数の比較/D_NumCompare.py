
ans = 0

#標準出力からのパラメータを入力
a,b = map(int,input().split())

# 入力された値が制約をみたしているかをチェック
while(a < 0 or a > 1001):
    a = int(input())

while (b < 0 or b > 1001):
    b = int(input())

# main処理

if ( a > b):
    ans = a
    print(ans)
elif ( a < b):
    ans = b
    print(ans)
elif ( a == b):
    ans = 'eq'
    print(ans)

