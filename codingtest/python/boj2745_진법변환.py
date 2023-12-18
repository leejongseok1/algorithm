import sys
input = sys.stdin.readline

n, b = input().rstrip().split()
n = n[::-1]

a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0

for i, j in enumerate(n):
    result += a.index(j) * (int(b) ** i)

print(result)