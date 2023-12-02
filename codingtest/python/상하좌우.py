'''
A는 N x N 정사각형 공간 위에 서 있다.
이 공간은 1 x 1 크기의 정사각형들로 나누어져있다.
가장 왼쪽 위 (1, 1), 가장 오른쪽 아래 (N, N)
L 왼쪽 R 오른쪽 U 위 D 아래
N x N 을 벗어나는 움직임은 무시됨
'''

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:

    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
