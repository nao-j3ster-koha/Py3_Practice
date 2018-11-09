# 入力する文字列長のパラメータを入力
num = int(input())

# 結果の文字列を格納する変数を初期化
rsltChar = ''

# 入力した文字列数まで、文字列を入力し、変数に文字列に格納する
for i in range(num):
    ch = input()
    rsltChar += ch

# 文字列変数の中身を表示
print(rsltChar)


