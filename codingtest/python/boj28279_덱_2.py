import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    command = list(map(int, input().split()))
    
    if command[0] == 1:         # 앞에 추가
        q.appendleft(command[1])
    elif command[0] == 2:       # 뒤에 추가
        q.append(command[1])
    elif command[0] == 3:       # 맨 앞 삭제
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command[0] == 4:       # 맨 뒤 삭제
        if q:
            print(q.pop())
        else:
            print(-1)
    elif command[0] == 5:       # 갯수
        print(len(q))
    elif command[0] == 6:       # empty
        if not q:
            print(1)
        else:
            print(0)
    elif command[0] == 7:       # 맨 앞 출력
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] == 8:       # 맨 뒤 출력
        if q:
            print(q[-1])
        else:
            print(-1)