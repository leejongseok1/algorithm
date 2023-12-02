'''
8 x 8 좌표 평면 (1~8) x (a~h)
나이트는 L 자로만 이동가능
1. 수평 2칸 이동 후 수직 1칸
2. 수직 2칸 이동 후 수평 1칸
평면 밖으로는 나갈 수 없음

현재 위치 입력 했을 때, 나이트가 이동할 수 있는 경우의 수 세기 ex) a1 - 2
'''

p = input()
row = int(p[1])
col = int(ord(p[0])) - int(ord('a')) + 1


cnt = 0

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

for step in steps:
    # 이동하고자 하는 위치 확인 
    next_row = row + step[0]
    next_col = col + step[1]

    # 해당 위치로 이동가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        cnt += 1

print(cnt)