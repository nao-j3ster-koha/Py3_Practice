Chr = input()

tChr = Chr[0]

if ( Chr.count(tChr) == len(Chr)):
    rslt = 'NG'
else:
    rslt = 'OK'

print(rslt)
