# データ文字列sと単位文字列nを入力して変数に格納
s,n = map(str, input().split())

#　変数の初期化
ans =''

#　入力データのチェック
while( int(s) < 1 or int(s) > 1000 ) and ( n != 'cm' or n != 'm' or n != 'km'):
    s, n = map(str, input().split)

#　単位に応じて答えの数値を計算
if( n == 'km'):
    ans = int(s) * 1000 * 1000
elif( n == 'm' ):
    ans = int(s) * 1000
elif( n == 'cm'):
    ans = int(s) * 10

#答えの文字列を表示
print(str(ans))




