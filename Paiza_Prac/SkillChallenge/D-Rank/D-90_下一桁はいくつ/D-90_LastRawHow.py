# ５つの数字をNumリストに空白で区切って格納
num = input().split(' ')

#合計値の初期化
total = 0

#Numリスト内の数値をそれぞれ足し合わせるループ
for i in num:
    total += int(i)

#Totalの数値を１０で譲与した数値を表示
print(total % 10)