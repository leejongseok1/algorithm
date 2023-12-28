# 1부터 n까지 중복없이 m개를 고른 수열
import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())

num = [i for i in range(1, n+1)]
result = list(permutations(num, m))

for i in result:
    print(*i)