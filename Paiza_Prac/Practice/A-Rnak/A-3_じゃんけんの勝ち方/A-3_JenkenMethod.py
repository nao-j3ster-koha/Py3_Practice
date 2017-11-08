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

# 相手の手をリスト化
for i in


