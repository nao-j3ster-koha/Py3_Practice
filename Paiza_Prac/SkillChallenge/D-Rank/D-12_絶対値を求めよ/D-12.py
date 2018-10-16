s1 = int(input())
ans = 0

while (s1 < -100 or s1 > 100):
    s1 = int(input())

if ( s1 < 0):
    ans = s1 * -1
else:
    ans = s1
print(str(ans))

