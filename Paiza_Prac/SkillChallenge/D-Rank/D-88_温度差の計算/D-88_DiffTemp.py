# 最高気温（tH),最低気温(tL)の数値を入力
tH, tL = map(int,input().split())

# 温度差の計算と計算結果の表示
diff = tH - tL
print(diff)
