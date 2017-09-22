
medal_list = ['Gold', 'Silver', 'Bronze']

country_list = []
for i in range(1, 4, 1):
    str = input()
    while ( int(len(str)) < 1 or int(len(str)) > 20):
        str = input()
    country_list.append(str)
    i += 1

for m in range(len(country_list)):
    print(medal_list[m] + ' '+ country_list[m])





