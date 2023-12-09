'''
n 장의 카드. 1~n까지의 번호
1번 제일 위 n번 제일 아래
제일 위 카드 버리고 제일 위 카드를 제일 아래로.
1234 : 1버림 234 - 2를 아래로 - 342 - 3버림 42 - 4 아래로 24 - 2버림 - 4남음
'''

import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque(range(1, n+1))

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])