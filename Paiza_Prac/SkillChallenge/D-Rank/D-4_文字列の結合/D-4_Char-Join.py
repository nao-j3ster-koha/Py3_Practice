
l_num = int(input())

while( l_num < 0 or l_num > 20):
    l_num = int(input())

str_list = []

for i in range(l_num):
    str1 = input()
    while ( len(str1) < 1 or len(str1) > 20):
        str1 = input()

    str_list.append(str1)
    i += 1

str_map = ' '
str_map = ','.join(str_list)

print("Hello, " + str_map + ".")


