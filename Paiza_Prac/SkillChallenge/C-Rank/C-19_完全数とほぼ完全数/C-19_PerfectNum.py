

def chkPfctNum(n):
    divList =[]
    # 入力値の約数リストの作成
    for t in range(1,n+1):
        if n % t == 0:
            divList.append(t)

    # 完全数か否かの確認
    tmpSum = 0
    for s in range(len(divList)-1):
        tmpSum += divList[s]

    if tmpSum == n:
        rslt = 'PerfectNumber'
    else:
        rslt = 'InperfectNumber'

    return rslt


src = int(input())

print(chkPfctNum(src))




