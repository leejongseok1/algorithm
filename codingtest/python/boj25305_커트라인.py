import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())
score = list(map(int, input().strip().split()))
score.sort(reverse=True)
print(score[k-1])