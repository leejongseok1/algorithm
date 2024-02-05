import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
trees = [int(input()) for _ in range(n)] # 4 2 6 12 18
gaps = []
for i in range(1, n):
    gaps.append(trees[i] - trees[i-1]) # 2 4 6 6

gaps_set = list(set(gaps))             # 2 4 6
gcd_num = gaps_set[0]                  # 2
for i in range(1, len(gaps_set)):
    gcd_num = gcd(gcd_num, gaps_set[i]) # 1: gcd_num = gcd(2, 4)
                                        # 2: gcd_num = gcd(2, 6)
                                        # gcd_num = 2
cnt = 0
for gap in gaps:  # 간격을 최대공약수로 나누고 -1 하면 심을 나무 숫자
    cnt += gap // gcd_num - 1
print(cnt)
