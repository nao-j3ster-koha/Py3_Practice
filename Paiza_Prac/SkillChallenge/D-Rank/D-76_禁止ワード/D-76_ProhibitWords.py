ngWord = input()
while ( len(ngWord) < 1 or len(ngWord) > 100 ):
    ngWord = input()

chkStrings = input()
while ( len(chkStrings) < 1 or len(chkStrings) > 100):
    chkStrings = input()

if ( chkStrings.count(ngWord) >= 1):
    rslt = 'NG'
else:
    rslt = chkStrings

print(rslt)



