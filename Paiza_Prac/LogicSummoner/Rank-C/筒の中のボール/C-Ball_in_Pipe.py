import re

# 変数の初期化

pos_R = 0
pos_L = 0
pos_list = []
result_list = []
result_string = ''

# 文字数指定のパラメータを入力

N = int(input())
while (N < 1 or N > 100):
    N = int(input())

# ボールの入れ方を指定する文字列を入力
p_chr = input()
while ((p_chr.count('L') + p_chr.count('R')) != N):
    p_chr = input()

for val in p_chr:
    pos_list.append(val)

pos_R = N - 1
for t in range(N):
    result_list.append(0)

for i in range(N):
    if (pos_list[i] == 'L'):
        if (pos_L == 0):
            result_list[0] = str(i + 1)
        else:
            for n in range(pos_L, -1, -1):
                result_list[n] = result_list[n - 1]
            result_list[0] = str(i + 1)
        pos_L += 1

    elif (pos_list[i] == 'R'):
        if (pos_R == N - 1):
            result_list[pos_R] = str(i + 1)
        else:
            for m in range(pos_R - 1, N - 1, 1):
                result_list[m] = result_list[m + 1]
            result_list[N - 1] = str(i + 1)
        pos_R -= 1
    i += 1

result_string = ' '.join(result_list)
print(result_string)