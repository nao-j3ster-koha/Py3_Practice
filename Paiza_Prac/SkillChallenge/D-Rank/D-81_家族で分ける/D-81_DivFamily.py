N = int(input())

H,W = map(int, input().split())

d = ( H * W) % N

print(d)
