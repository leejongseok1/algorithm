import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()
for _ in range(n):
    operation = sys.stdin.readline().split()

    if operation[0] == 'push':
        queue.append(operation[1])
    elif operation[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif operation[0] == 'size':
        print(len(queue))
    elif operation[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else: 
            print(0)
    elif operation[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif operation[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])