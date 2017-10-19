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

seed = 200

def rand1_1():
    A = 5
    C = 1
    M = 8
    global seed
    seed = ( A * seed + C ) % M
    return seed

for i in range(15):
    print("%2d", rand1_1())







