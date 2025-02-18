import sys
N, M, K = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num = sorted(num)
first = num[-1]
second = num[-2]
sum = 0
for i in range(M):
    if i != 0 and i % K == 0:
        sum += second
    else: 
        sum += first
    
print(sum)