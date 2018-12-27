dog_cnt = 0
cat_cnt = 0

for i in range(0,3):
    s_i = input()
    if ( s_i == 'dog'):
        dog_cnt += 1
    else:
        cat_cnt += 1

if ( dog_cnt > cat_cnt ):
    print('dog')
else:
    print('cat')

