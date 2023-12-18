import sys
input = sys.stdin.readline

n, b = input().rstrip().split()
n = n[::-1]

a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0

for i, j in enumerate(n):
    result += a.index(j) * (int(b) ** i)

print(result)


# int를 사용하면 b진법을 10진법으로 풀어줌
# n, b = map(str, input().split())
# print(int(n, int(b)))