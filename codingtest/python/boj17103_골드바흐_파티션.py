# "어떤 수에 대해, 그 수를 두 소수의 합으로 표현하는 방법의 경우의 수를 그 수의 골드바흐 수라고 부른다"

import sys
input = sys.stdin.readline

arr = [1] * 1000001
arr[0], arr[1] = 0, 0

for i in range(2, 1000001):
    if arr[i]:
        for j in range(i*2, 1000001, i):
            arr[j] = 0
            
T = int(input())
for i in range(T):
    cnt = 0
    n = int(input())
    for j in range(2, n//2+1):
        if arr[j] and arr[n-j]:
            cnt += 1
    print(cnt)