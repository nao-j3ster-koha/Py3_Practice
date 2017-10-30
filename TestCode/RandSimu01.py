from datetime import datetime

# 線形合同法
#️ 漸化式 Xi = ( A * Xi-1 + C ) mod M
# Mが２の累乗の場合は Aを A mod 8 が 5 または3になるような数値を設定する
# 定数項が取りうる範囲は M>A、M>C、A>0、C≥0
# C は奇数が良い
# Xi-1は初期値でSeedとも呼ぶ（一律「1」とする）

## 定数項の検討
# パターン１ M = 8, A = 5, C = 1
# パターン２ M = 8, A = 5, C = 3
# パターン３ M = 8, A = 5, C = 5
# パターン４ M = 8, A = 5, C = 7

# パターン１の乱数生成

seed0 = 1509094800
seed1 = 1509094800
clockChar = datetime(2017,10,26,18,00,00)
epochnum = int(datetime(2017,10,30,18,00,00).timestamp())


seedList = [epochnum * 1, epochnum * 30, epochnum * 10 , epochnum * 2017 ]
seedList1 = [epochnum * 2017, epochnum * 10, epochnum * 30, epochnum * 1]
#seedList1 = [epochnum * 5, epochnum * 27, epochnum * 10, epochnum * 2017]



def lcg01(n):
    A = 1664525
    C = 1013904223
    M = 0xffffffff
    n = int(( A * n + C )) & M
    return n % 32768
#    return ( n / 65536 ) % 32768


def rand1(n):
    global seed1
    M = 2 ** 31 -1
    n = int((n * 1103515245 + 12345)) & M
    return n % 32768
#    return ( n / 65536 ) % 32768



rslt_lcg01 = ''
rslt_rand1 = ''
rslt_rand2 = ''

for i in range(4):
    tmp0 = int(lcg01(seedList[i]) % 10)
    rslt_lcg01 += str(tmp0)

    tmp1 = int(rand1(seedList1[i]) % 10)
    rslt_rand1 += str(tmp1)

print('lcg01: ', rslt_lcg01)
print('rand1: ', rslt_rand1)









