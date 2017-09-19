# 地図データの入力
s = input()
while ( len(s) < 1 or len(s) > 100 ) or ( ( s.count('0') + s.count('1')) > len(s) ):
    s = input()

# 体力の入力
t = int(input())
while ( t < 1 or t > 100):
    t = int(input())

for i in range(len(s)):
    if(s[i] == '1'):
        t -= 1

if(t > 0):
    print(str(t))
else:
    print('No')




