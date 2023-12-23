import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

num = sorted([a, b, c])
while num[0] + num[1] <= num[2]:
    num[2] -= 1

area = sum(num)
print(area)