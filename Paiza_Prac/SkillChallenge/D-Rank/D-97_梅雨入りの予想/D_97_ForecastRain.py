list = input().split()
count = 0

for dt in list:
    if int(dt) == 1:
        count += 1

if count >= 5:
    print('yes')
else:
    print('no')