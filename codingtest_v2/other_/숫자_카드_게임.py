import sys
n, m = map(int, sys.stdin.readline().split())

li = []
for _ in range(n):
    num = list(map(int, sys.stdin.readline().split()))
    li.append(min(num))

print(max(li))