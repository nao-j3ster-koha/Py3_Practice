# パラメータデータの入力
# グループの数と、グループの数を入力
tblLength, grpNum = map(int, input().split())
while ( tblLength < 1 or tblLength > 100) or (grpNum < 1 or grpNum > 100):
    tblLength, grpNum = map(int, input().split())

srcList = []

#各グループの着席開始位置と、必要席数についてのソースリストを作成
for i in range(grpNum):
    prsnNum, chairPos =map(int, input().split())
    srcList.append([prsnNum, chairPos])

#テーブルの状態管理用リストの初期化
sitNum = 0
tblStatus = []
for i in range(tblLength):
    tblStatus.append(0)


customerNum = 0

for k in range(grpNum):
    prsnNum = srcList[k][0]
    chairPos = srcList[k][1]
    rcvrPos = srcList[k][1]
    sitStatus = 0

    # 各リスト内の着席開始位置から必要数の座席が空いているか否かのチェック
    for m in range(chairPos-1,chairPos-1+prsnNum,1):
        if( m >= tblLength):
            m -= tblLength
        if ( tblStatus[m] == 0):
            sitStatus += 1

    # 空席状況のチェック結果を確認→必要に応じて着席状況の更新
    if ( prsnNum == sitStatus):
        customerNum += prsnNum
        for n in range(rcvrPos-1,rcvrPos-1+prsnNum ,1):
            if( n >= tblLength):
                n -= tblLength
            tblStatus[n] = 1

#        print(str(customerNum))

print(str(customerNum))
