# 메모리초과(sort, sorted)
# 계수정렬 이용

import sys
input = sys.stdin.readline

n = int(input())
num = [0] * 10001

for _ in range(n):
    num[int(input())] += 1
    
for i in range(len(num)):
    if num[i] != 0:
        for _ in range(num[i]):
            print(i)