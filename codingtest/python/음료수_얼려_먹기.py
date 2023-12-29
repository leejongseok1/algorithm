'''
N x M 크기의 얼음 틀
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1
구멍이 뚫려 있는 부분끼리 상하좌우로 붙어있는 경우 서로 연결되어 있는 것으로 간주
얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
4 x 5 의 얼음 틀 예시에서는 아이스크림이 총 3개가 생성된다.

0끼리 붙어있는 것은 하나의 덩이가 만들어짐 - 아이스크림.

연결 요소 찾기 문제

1. 특정 지점의 상하좌우를 살핀 뒤 주변 지점 중 값이 0이면서 아직 방문하지 않은 지점이 있다면
해당 지점을 방문한다.
2. 방문한 지점에서 다시 상하좌우를 살펴보면서 방문 과정을 반복하면 연결된 모든 지점 방문 가능
3. 방문하지 않은 지점의 수 카운트
'''

import sys
from collections import deque
input = sys.stdin.readline

def dfs(x, y):
    # 범위 벗어나는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상하좌우 모두 재귀 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

n, m = map(int, input().strip().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

# 모든 노드에 대하여 음료수 채우기
icecream = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        # 처음 방문한 곳이라면 값 증가
        if dfs(i, j) == True:
            icecream += 1

print(icecream)