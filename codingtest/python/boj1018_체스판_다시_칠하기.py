import sys
input = sys.stdin.readline
# n 10 m 13
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

cnt = []

# n - 7 = 3 / m - 7 = 6
for i in range(n-7):
    for j in range(m-7):
        black = 0 # 'W'로 시작할 경우 바뀐 체스판 갯수
        white = 0 # 'B'로 시작할 경우 바뀐 체스판 갯수

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'B':
                        black += 1
                    if board[a][b] != 'W':
                        white += 1
                
                else:
                    if board[a][b] != 'B':
                        black += 1
                    if board[a][b] != 'W':
                        white += 1

        cnt.append(black)
        cnt.append(white)

print(min(cnt))

