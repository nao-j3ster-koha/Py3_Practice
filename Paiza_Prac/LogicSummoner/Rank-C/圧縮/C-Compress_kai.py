# 変数の初期化
srcList= []
srcStrings = ''
rsltStrings = ''
preString = ''
rsltList = []
b_cnt = 0
w_cnt = 0
s_pos = 0

# 文字列の入力
srcStrings = input()

#　文字列が条件を満たしているかをチェック
while((len(srcStrings) < 1 or len(srcStrings) > 100) \
              or (srcStrings.count('b') + srcStrings.count('w') != len(srcStrings)  )):
    srcStrings = input()

# 文字列を一時的にリスト化
for val in srcStrings:
    srcList.append(val)

# 最初の文字列を判別
if(srcList[0] == 'w'):
    preString = '0 '
else:
    preString = ''


# 文字列の検査
while( s_pos < len(srcList)):
    if(srcList[s_pos] == 'b'):
        b_cnt = 1
        s_pos += 1
        while( s_pos + 1 <= len(srcList)) and ( srcList[s_pos -1] == srcList[s_pos]):
            b_cnt += 1
            s_pos +=1
        rsltList.append(str(b_cnt))
    else:
        w_cnt = 1
        s_pos += 1
        while( s_pos +1 <= len(srcList)) and ( srcList[s_pos -1] == srcList[s_pos]):
            w_cnt += 1
            s_pos += 1
        rsltList.append(str(w_cnt))

rsltStrings = ' '.join(rsltList)
print(preString + rsltStrings)



