dispCard = ''

for i in range(4):
    num = int(input())
    while ( num < 1 or num > 5):
        num = int(input())
    dispCard = dispCard + str(num)
    i += 1

for i in range(len(dispCard)+1):
    if ( (str(i+1) in dispCard) == False):
#    if ( dispCard.count(str(i+1)) != 1):
        m = i + 1
    else:
        pass

print(m)
