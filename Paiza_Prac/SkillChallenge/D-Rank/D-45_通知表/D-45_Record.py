num = int(input())

while ( num < 1 or num > 5):
    num = int(input())

if( num == 5):
    rslt = 'A'
elif( num == 4):
    rslt = 'B'
elif( num == 3 ):
    rslt = 'C'
elif( num == 2):
    rslt = 'D'
elif( num == 1):
    rslt = 'E'

print(rslt)