import re

Char = input()

if ( ('i' in Char) or ( 'l' in Char) or ( 'I' in Char)):
    chkFalg = 1

if chkFalg == 1:
    print('caution')
else:
    print(Char)
