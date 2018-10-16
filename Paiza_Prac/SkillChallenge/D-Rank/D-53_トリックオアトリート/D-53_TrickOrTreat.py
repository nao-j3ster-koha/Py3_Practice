str = input()
while (int(len(str)) < 1 or int(len(str)) > 20):
    str = input()

if ( str == 'chocolate' or str == 'candy'):
    rslt = 'Thanks!'
else:
    rslt = 'No!'

print(rslt)