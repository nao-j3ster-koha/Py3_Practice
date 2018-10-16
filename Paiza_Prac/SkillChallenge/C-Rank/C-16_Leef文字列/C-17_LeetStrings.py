String1 = input()
while (len(String1) < 1 or len(String1) > 100):
    String1 = input()

dtList = [ ['A', '4'], ['E', '3'], ['G', '6'], ['I', '1'], ['O', '0'], [ 'S' , '5'], ['Z', '2']]

for i in range(len(dtList)):
    String1= String1.replace(str(dtList[i][0]),str(dtList[i][1]))
print(String1)

