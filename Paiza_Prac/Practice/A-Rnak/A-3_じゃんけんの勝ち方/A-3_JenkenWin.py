import itertools

# 変数の初期化

rndNum = 0      #じゃんけんの回数
fngTtl = 0      #出した指の合計数
fngStr = ''     #相手が出す手


while( rndNum < 1 or rndNum > 1000) or ( fngTtl < 0 or fngTtl > 5000):
    rndNum, fngTtl = map(int,input().split())


while( len(fngStr) < 1 or len(fngStr) > rndNum ) or ( ( fngStr.count('G') + fngStr.count('C') + fngStr.count('P')) != rndNum ):
    fngStr = input()

# 相手の出した手に対して勝つことのできる手を文字列で出力
def judgeStr(x):
    rChr = ''
    for i in range(len(x)):
        if x[i] == 'G':
            y = 'P'
            rChr += y
        elif x[i] == 'C':
            y = 'G'
            rChr += y
        else:
            y = 'C'
            rChr += y
    return rChr

# 勝つことのできる手で計数した場合の出す手の合計
def countFingNum(m):
    totalNum = 0
    winCount = 0
    for i in range(len(m)):
        if m[i] == 'G':
            k = 0
            totalNum += k
            winCount += 1
        elif m[i] == 'C':
            k = 2
            totalNum += k
            winCount += 1
        else:
            k = 5
            totalNum += k
            winCount += 1
    return totalNum, winCount




# 検討後のロジック


"""
1:パラメータの入力
 ラウンド数：         rndNum
 出せる指の合計数：    cntFingNum
 相手が出す手の文字列: enmFingStr

空で初期化するパラメータ
 相手が出す手のリスト：       enmFingList
 勝った回数:                 winCount
 相手に出す手のリスト：        cntFingList
 勝っている間出した指の小計:   cntFingCount
 相手の手がチョキのIndexリスト：indxC
 相手の手がパーのIndexリスト：indxP
 相手の手がぐーのIndexリスト：indxG

2:相手の手をリストに格納
 enmFingStr ー＞ enmFingList

3:相手の手数を同じ数で自分の手のリストを初期化
 cntFingList ー＞ 'N'で初期化

4:相手の手が「’C’」の場合の自分手のリスト更新と勝利回数の更新
 相手の手が'C'のリスト内Indexを取得
 indxC = [ i for i,x in enumerate(enmFingList) if x == 'C' ]
 for i in indxC:
    cntFingList[i] = 'G'













cntStr = judgeStr(fngStr)

print(countFingNum(cntStr))












