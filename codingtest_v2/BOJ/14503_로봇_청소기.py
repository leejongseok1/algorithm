import sys
N, M = map(int, sys.stdin.readline().split())

x, y, direction = map(int, sys.stdin.readline().split())
d = [[0] * M for _ in range(N)] # 방문한 위치 저장하기 위한 맵
d[x][y] = 1 # 현재 좌표 방문 처리

array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))
    
# 북, 동, 남, 서 방향 정의
d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0
while True:
    # 기본 동작
    turn_left()
    nx = x + d_row[direction]
    ny = y + d_col[direction]
    
    if array[nx][ny] == 0 and d[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - d_row[direction]
        ny = y - d_col[direction]
        
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)