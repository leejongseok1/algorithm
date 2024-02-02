import sys
input = sys.stdin.readline

# 이진 탐색 - 성공 (2460 ms / 115508 KB)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return cnt.get(target)
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
num_cards = sorted(list(map(int, input().split())))
m = int(input())
m_cards = list(map(int, input().split()))

cnt = {}
for i in num_cards:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in m_cards:
    print(binary_search(num_cards, i, 0, len(num_cards)-1), end=' ')

# dictionary 이용 - 성공 (832 ms / 119756 KB)
# -------------------------------------------
# n = int(input())
# num_cards = list(map(int, input().split()))
# m = int(input())
# m_cards = list(map(int, input().split()))

# cnt = {}
# for i in num_cards:
#     if i in cnt:
#         cnt[i] += 1
#     else:
#         cnt[i] = 1
        
# for i in m_cards:
#     if i in cnt:
#         print(cnt[i], end=' ')
#     else:
#         print(0, end=' ')
# -------------------------------------------

# 1차 시도 -> 시간초과
# -------------------------------------------
# n = int(input())
# num_cards = list(map(int, input().split()))
# m = int(input())
# m_cards = list(map(int, input().split()))

# cnt = [0 for _ in range(m)]
# for i in range(len(m_cards)):
#     for j in range(len(num_cards)):
#         if m_cards[i] == num_cards[j]:
#             cnt[i] += 1

# print(' '.join(cnt))
# -------------------------------------------

# 2차 시도 -> 시간초과
# -------------------------------------------
# n = int(input())
# num_cards = list(map(int, input().split()))
# m = int(input())
# m_cards = list(map(int, input().split()))

# cnt = [0 for _ in range(m)]

# for i in range(len(m_cards)):
#     cnt[i] += num_cards.count(m_cards[i])

# print(' '.join(cnt))
# -------------------------------------------