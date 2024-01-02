def solution(park, routes):
    
    h = len(park)
    w = len(park[0])
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    move_types = ['W', 'E', 'N', 'S']

    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j

    for route in routes:
        
        direction, distance = route.split()
        distance = int(distance)
        flag = 0
        nx = x
        ny = y

        for i in range(1, distance+1):
            nx += dx[move_types.index(direction)]
            ny += dy[move_types.index(direction)]

            if nx < 0 or ny < 0 or nx >= h or ny >= w or park[nx][ny] == 'X':
                flag = 1
                break
        
        if flag == 0:
            x += dx[move_types.index(direction)] * distance
            y += dy[move_types.index(direction)] * distance

    return [x, y]