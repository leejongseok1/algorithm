import sys
input = sys.stdin.readline

limit = 123456

arr = [1] * (2 * limit + 1)
arr[0], arr[1] = 0, 0

for i in range(2, int(len(arr)**0.5)+1):
    if arr[i]:
        for j in range(i + i, len(arr), i):
            arr[j] = 0

while True:
    n = int(input())
    if n == 0: break
    # else:
    #     print(sum(arr[n+1:(2*n)+1]))
    
    cnt = 0
    for i in range(n+1, 2*n+1):
        if arr[i] != 0:
            cnt += 1
    print(cnt)