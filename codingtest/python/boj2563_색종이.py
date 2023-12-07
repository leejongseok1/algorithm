n = int(input())

square = [[0 * 100 for _ in range(101)] for _ in range(101)] # 2차원 배열 선언

for _ in range(n):
    x, y = list(map(int, input().split()))

    for row in range(x, x+10): 
        for col in range(y, y+10):
            square[row][col] = 1  # 방문한 픽셀 1로 update

area = 0
for i in range(101):
    area += square[i].count(1)

print(area)

