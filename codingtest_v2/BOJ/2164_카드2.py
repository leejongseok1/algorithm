import sys
from collections import deque

N = int(sys.stdin.readline())
card = deque(range(1, N+1))

for i in range(len(card)):
    
    if len(card) == 1:
        print(card[0])

    else:
        card.popleft()
        card.append(card.popleft())