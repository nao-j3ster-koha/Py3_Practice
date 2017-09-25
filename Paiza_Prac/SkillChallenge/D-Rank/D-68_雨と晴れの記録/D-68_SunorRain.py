
n = int(input())
while ( n < 1 or n > 100):
    n = int(input())

str1 = input()
while ( len(str1) < 1 or len(str1) > n) \
        or( str1.count('S') + str1.count('R') != len(str1)):
    str1 = input()


print(str(str1.count('S')) + ' ' + str(str1.count('R')))
