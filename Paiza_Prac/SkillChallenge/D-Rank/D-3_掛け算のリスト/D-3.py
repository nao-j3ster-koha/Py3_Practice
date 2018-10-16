n = int(input())


while( n <0 or n > 100):
    n = int(input())

ans = []

for i in range(10):
    ans.append(str(n * (i+1)))
    i += 1

print(ans)
ans_string = ' '.join(ans)

#ans_string_list = map(str, ans)

#ans_string = ' '.join(ans_string_list)
print(ans_string)
