num = int(input())

while ( num < 1 or num > 100):
    num = int(input())

sum = 0
for i in range(num):
    m = i + 1
    sum += m

print(sum)
