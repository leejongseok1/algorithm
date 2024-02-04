import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
# 분자, 분모
num1, den1 = list(map(int, input().split()))
num2, den2 = list(map(int, input().split()))

num = num1 * den2 + num2 * den1
den = den1 * den2

gcd1 = gcd(num, den)
num //= gcd1
den //= gcd1

print(num, den)