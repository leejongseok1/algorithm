import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
a = set(input().split())
b = set(input().split())

print(len(a - b) + len(b - a))