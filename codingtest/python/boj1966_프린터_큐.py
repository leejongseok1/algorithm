import sys
from collections import deque

T = int(sys.stdin.readline().strip()) # testcase num

for i in range(T):
    n, m = map(int, sys.stdin.readline().strip().split())
    priority = deque(list(map(int, sys.stdin.readline().strip().split())))

    cnt = 0
    while priority:
        if priority[0] == max(priority): # 맨 앞이 중요도 top 이라면
            cnt += 1                     # 출력되므로 cnt++
            priority.popleft()           # 제거
            if m == 0:
                break
        else:                                   # 중요도가 나중순위라면
            priority.append(priority.popleft()) # 맨 뒤로
        
        if m > 0:
            m = m - 1
        else:
            m = len(priority) - 1

    print(cnt)








