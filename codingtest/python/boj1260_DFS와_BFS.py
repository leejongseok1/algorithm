# n 정점의 갯수  m 간선의 개수, v 시작 번호
import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().strip().split())

graph = [[] for i in range(n+1)]
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().strip().split())
    
    graph[a] += [b]
    graph[b] += [a]

def dfs(graph, v, visited):
    
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                
                
dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)