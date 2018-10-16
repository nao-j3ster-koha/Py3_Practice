src_data = []

N = int(input())
while( N<0 ):
    N = int(input())


for i in range(1,N+1):
    src_data.append(i)

for n in range(len(src_data)):
    check_fizz = int(src_data[n]) % 3
    check_buzz = int(src_data[n]) % 5

    if(check_fizz == 0 and check_buzz == 0):
        src_data[n] = "Fizz Buzz"
    elif(check_fizz == 0):
        src_data[n] = "Fizz"
    elif(check_buzz == 0):
        src_data[n] = "Buzz"
    print(src_data[n])




