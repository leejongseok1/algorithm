import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
clothes = [i+1 for i in range(N)]
print(len(list(combinations(clothes, 2)))*2)
# print(N * (N - 1))