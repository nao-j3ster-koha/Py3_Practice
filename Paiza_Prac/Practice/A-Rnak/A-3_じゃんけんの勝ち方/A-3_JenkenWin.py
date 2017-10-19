# 変数の初期化

rndNum = 0      #じゃんけんの回数
fngTtl = 0      #出した指の合計数
fngStr = ''     #相手が出す手


while( rndNum < 1 or rndNum > 1000) or ( fngTtl < 0 or fngTtl > 5000):
    rndNum, fngTtl = map(int,input().split())


while( len(fngStr) < 1 or len(fngStr) > rndNum ) or ( ( fngStr.count('G') + fngStr.count('C') + fngStr.count('P')) != rndNum ):
    fngStr = input()










