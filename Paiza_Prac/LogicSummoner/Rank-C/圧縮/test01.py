#tstStrings = 'bbbbwwbbwbwbbwbbwbwbbw'
tstStrings = 'wwwwbbwwbbb'
# bbbb ww bb w b w bb w bb w b w bb w
# 4 2 2 1 1 1 2 1 2 1 1 2 1
#tstStrings = 'bbbbwwbb'
tstList = []
rsltList = []
b_cnt = 0
w_cnt = 0
s_pos = 0

# 文字列をリストに格納
for i in range(len(tstStrings)):
    tstList.append(tstStrings[i])

# 先頭の文字列を判別
if(tstList[0] == 'w'):
    preString='0 '
else:
    preString=''


# 文字列リスト内をパース
#for s_pos in range(len(tstList)-1):
while( s_pos < len(tstList)):
    if(tstList[s_pos] == 'b'):
        b_cnt = 1
        s_pos += 1
        while ( (s_pos + 1  <= len(tstList)) and (tstList[s_pos-1] == tstList[s_pos]) ):
            b_cnt += 1
            s_pos += 1
        rsltList.append(str(b_cnt))
#        s_pos += 1
        print(rsltList)
    else:
        w_cnt = 1
        s_pos += 1
        while((s_pos+1 <= len(tstList)) and (tstList[s_pos-1] == tstList[s_pos])):
            w_cnt += 1
            s_pos += 1
        rsltList.append(str(w_cnt))
#        s_pos += 1
        print(rsltList)

sufStrings=' '.join(rsltList)

print(preString + sufStrings)


