import sys
input = sys.stdin.readline
            
def eratosthenes(m, n):
    arr = [i for i in range(n+1)]
    end = int(n**0.5) # n의 제곱근
    for i in range(2, end+1):
        # 소수가 아닌 수는 pass
        if arr[i] == 0:
            continue
        # 자기 자신 제외한 i의 배수 0으로 처리
        for j in range(i*i, n+1, i):
            arr[j] = 0
    
    primes = []
    for i in range(max(2, m), n+1):
        if arr[i] != 0:
            primes.append(i)
    return primes

m, n = map(int, input().split())
primes = eratosthenes(m, n)
for prime in primes:
    print(prime)

# m, n = map(int, input().split())
# for i in range(m, n+1):
#     if i == 1:
#         continue
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             break
#     else:
#         print(i)