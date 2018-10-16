m, n = map(int, input().split())

while(m < 1 or m > 100):
    m = int(input())

while (n < 1 or n >100):
    n = int(input())


result_list = []
tmp_result = 0
result_string = ''

for i in range(10):
    tmp_result = m + n * i
    result_list.append(str(tmp_result))

result_string = ' '.join(result_list)
print(result_string)

