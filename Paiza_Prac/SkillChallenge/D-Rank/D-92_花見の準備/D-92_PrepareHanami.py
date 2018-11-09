# 1組目のシートサイズと値段を入力
l1,w1,p1 = map(int,input().split())
# 2組目のシートサイズと値段を入力
l2,w2,p2 = map(int,input().split())

#それぞれのシートの単位面積当たりの単価を算出
cp1 = p1 / ( l1 * w1)
cp2 = p2 / ( l2 * w2)

#　2組のシート単価を比較した結果に応じた内容を表示
if cp1 < cp2:
    print(str(l1) + ' ' + str(w1) + ' ' + str(p1))

elif cp1 > cp2:
    print(str(l2) + ' ' + str(w2) + ' ' + str(p2))

else:
    print('DRAW')


