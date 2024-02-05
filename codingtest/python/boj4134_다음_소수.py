import sys
input = sys.stdin.readline

# N의 제곱근 까지만 나눠서 소수 판별
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    num = int(input())
    while True:
        if num == 0 or num == 1:
            print(2)
            break
        if is_prime(num):
            print(num)
            break
        else:
            num += 1