'''
R x C 목장
비어있거나 양 or 늑대가 있음
늑대는 인접한 칸 자유롭게 이동

목장에 울타리를 설치해 늑대가 양이 있는 칸으로 갈 수 없게
울타리를 설치하자

Input 

R x C
R 개줄의 목장 상태 . :빈칸 / s:양 / w:늑대

Output
늑대가 양이 있는 칸으로 갈 수 없게 할 수 있다면 1 출력 후
목장 상태 출력 . 울타리 D

울타리 어떻게 설치해도 늑대가 양이 있는 칸으로 갈 수 있다면 0 출력
'''

import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().strip().split())
for _ in range(r):
    farm = input().strip()

graph = [[] for i in range(c+1)]
visited = [0] * (c+1)

def bfs(x, y):
    
    if x <= -1 or x >= r or y <= -1 or y >= c:
        return False

# .빈칸 S양 W늑대    
    if graph[x][y] != 'W':
        