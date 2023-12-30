import sys
input = sys.stdin.readline

n = int(input()) # 노드 개수(컴퓨터 수)
m = int(input()) # 연결선 수(간선 수)
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    
    a, b = map(int, input().strip().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

dfs(1)
print(sum(visited)-1) # 1번 컴퓨터를 제외하고 1번 컴퓨터와 연결된 개수 출력