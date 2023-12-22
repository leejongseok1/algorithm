import sys

n, k = map(int, sys.stdin.readline().strip().split())

div = []

for i in range(1, n+1):
    if n % i == 0:
        div.append(i)

if len(div) >= k:
    print(div[k-1])
else:
    print(0)