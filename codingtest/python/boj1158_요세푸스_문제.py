# deque() ver.
from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n+1))
remove_list = []

while q:
    for _ in range(k-1):
        q.append(q.popleft())

    remove_list.append(q.popleft())

print(str(remove_list).replace('[', '<').replace(']', '>'))

# list ver.