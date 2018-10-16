wordA = input()
wordB = input()

if ( wordA[-1] == wordB[0]) and ( wordB[-1] != 'n'):
    rslt = 'OK'
else:
    rslt = 'NG'

print(rslt)

