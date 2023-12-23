import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

choice = list(combinations(num, 3))

sum_filter = [sum(i) for i in choice if sum(i) <= m]

print(max(sum_filter))