# 10日間の花粉量データを入力し、文字列リストに格納
data = input().split()

#外出可能な日数の変数を初期化
go = 0

#dataリスト内をチェックして、花粉量の数値が２以下の場合は外出日数を１日増やす
for i in range(len(data)):
    if int(data[i]) <= 2:
        go += 1

#外出可能な日数を表示する
print(go)
