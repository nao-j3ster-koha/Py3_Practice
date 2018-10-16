import re

tag1,tag2 = map(str, input().split())

while ( len(tag1) < 3 or len(tag1) > 100 ) \
    or ( len(tag2) < 3 or len(tag2) > 100):
    tag1,tag2 = map(str, input().split())

tgtStrings = input()
while ( len(tgtStrings) < 6 or len(tgtStrings) > 5000):
    tgtStrings = input()


while( tgtStrings.count(tag1) != 0 )  and ( tgtStrings.count(tag2) != 0):
    t1_pos = re.search(tag1, tgtStrings).end()
    t2_pos = re.search(tag2, tgtStrings).start()
    if ( t2_pos - t1_pos == 0):
        rslt = '<blank>'
        print(rslt)
    else:
        rslt = tgtStrings[t1_pos:t2_pos]
        print(rslt)
    nxt_pos = re.search(tag2, tgtStrings).end()
    tgtStrings = tgtStrings[nxt_pos:]







