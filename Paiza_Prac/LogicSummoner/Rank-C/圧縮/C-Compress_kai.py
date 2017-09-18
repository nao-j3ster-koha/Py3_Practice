
srcStrings = input()

while((len(srcStrings) < 1 or len(srcStrings) > 100) or (srcStrings.count('b') + srcStrings.count('w') != len(srcStrings)  )):
    srcStrings = input()

tmp_list = []
result_string = ''

for val in srcStrings:
    tmp_list.append(val)

result_list = []

if(srcStrings[0] == 'w'):
    result_list.append(0)

line_pos = 0
b_cnt = 0
w_cnt = 0


for i in range(len(tmp_list)):
    if(tmp_list[i] == 'b'):
        b_cnt +=1
        n = i
        while( tmp_list[n+1] == tmp_list[n]):
            b_cnt += 1
            n += 1
        result_list.append(b_cnt)
        i = n
    else:
        w_cnt += 1
        m = i
        while( tmp_list[m+1] == tmp_list[m]):
            w_cnt += 1
            m += 1
        result_list.append(w_cnt)

result_string = ' '.join(result_list)
print(result_string)






