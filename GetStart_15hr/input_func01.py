def input_strings():
    argStr1, argStr2 = map(str, input().split())
    while ( len(argStr1) < 1 or len(argStr1) > 10) or ( len(argStr2) < 1 or len(argStr2) > 10):
        print('入力文字数が制限を超えています')
        argStr1, argStr2 = map(str, input().split())
    return (argStr1, argStr2)

if __name__ == "__main__":
    a = input_strings()

    print('第1引数 {0}, 第2引数 {1}'.format(a[0], a[1]))
