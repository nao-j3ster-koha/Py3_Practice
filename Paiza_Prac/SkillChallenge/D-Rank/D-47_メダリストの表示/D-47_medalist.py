
medal_list = ['Gold', 'Silver', 'Bronze']

country_list = []
for i in range(3):
    str = input()
    while ( int(len(str)) < 1 or int(len(str)) > 20):
        str = input()
    country_list.append(str)
#    i += 1

#通常のループ変数からのリスト参照
for m in range(len(country_list)):
    print('Normal-Loop ' + medal_list[m] + ' '+ country_list[m])

#enumerate関数を使用したリスト参照
for indx, cntryName in enumerate(country_list):
    print('enum {0} {1}'.format(medal_list[indx],cntryName))

#zip関数を使用した2つのリストの参照
for cntryName,medalColor in zip(country_list, medal_list):
    print('zip {0} {1}'.format(medalColor,cntryName))



