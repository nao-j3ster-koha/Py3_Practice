r1,r2 = map(int, input().split())

while(r1 < 1 or r1 > 20) or (r2 < 1 or r2 > 20) or ( r1 < r2):
    r1,r2 = map(int, input().split())


ans = (r1 ** 3) - ( r2 ** 3 )

print(ans)
