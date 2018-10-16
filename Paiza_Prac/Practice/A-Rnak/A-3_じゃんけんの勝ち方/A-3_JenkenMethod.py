#ラウンド数と出せる指の合計数を入力

rndNum,cntFingNum = map(int, input().split())

# 相手が出す手の文字列を入力
enmFingStr = input()

#パラメータの初期化

enmFingList = []    # 相手が出す手のリスト形式
cntFingList = []    # 相手に出す手のリスト形式
indxC = []          # 相手の手のうち「チョキ」のリスト内インデックス
indxP = []          # 相手の手のうち「パー」のリスト内インデックス
indxG = []          # 相手の手のうち「グー」のリスト内インデックス

winCount = 0        # 相手に勝った回数
cntFingCount = 0    # 相手に出した指の合計

# 相手の手をリスト化(enmFingList),自分の手リストを初期化（cntFingList)
for i in range(len(enmFingStr)):
    enmFingList.append(enmFingStr[i])
    cntFingList.append('N')

# 相手の手が「C」の場合のカウント
indxC = [ i for i,x in enumerate(enmFingList) if x == 'C']

for t in indxC:
    cntFingList[t] = 'G'
    winCount += 1

# 相手の手が「P」の場合のカウント
indxP = [ n for n,y in enumerate(enmFingList) if y == 'P']
for t in indxP:
    if cntFingCount <= cntFingNum:
        cntFingList[t] = 'C'
        winCount += 1
        cntFingCount += 2
    else: cntFingList[t] = 'G'

# 相手の手が「G」の場合のカウント
indxG = [ m for m,z in enumerate(enmFingList) if z == 'G']

for t in indxG:
    if cntFingCount < cntFingNum:
        cntFingList[t] = 'P'
        winCount += 1
        cntFingCount += 5
    else: cntFingList[t] = 'C'


print(winCount)
print(cntFingCount)





