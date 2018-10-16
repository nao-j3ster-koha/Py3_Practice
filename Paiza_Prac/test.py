alList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']

S1 = input()
while (S1 not in alList):
    S1 = input()

cnt = 1
#for i in range(len(alList)):
while (S1 != alList[i]):
    cnt += 1

print(str(cnt))
