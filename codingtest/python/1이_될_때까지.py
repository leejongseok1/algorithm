'''
n을 1로 만드는 최소 횟수
1. n에서 1을 뺌
2. n을 k로 나눔 (n이 k로 나누어 떨어질 때만 가능)
'''

n, k = map(int, input().split())

cnt = 0

# my
while True:

    if n % k == 0:
        n /= k
        cnt += 1
    elif n % k != 0:
        n -= 1
        cnt += 1
    if n == 1:
        break

print(cnt)

'''
# solution
while n >= k:
    while n % k != 0:
        n -= 1
        cnt += 1
    n //= k
    cnt += 1
    
while n > 1:
    n -= 1
    cnt += 1
    
print(cnt)
'''
