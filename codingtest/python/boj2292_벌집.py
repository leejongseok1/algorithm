import sys

n = int(sys.stdin.readline())

cnt = 1 # 지나온 방 갯수
room = 1 # 벌집 갯수

while n > room:
    room += 6 * cnt # 벌집이 6의 배수씩 증가
    cnt += 1

print(cnt)


'''
import sys

n = int(sys.stdin.readline())

cnt = 1 # 지나온 방 갯수
room = 2 # 벌집 갯수

if n == 1:
    print(1)
else:
    while (room <= n):
        room += 6 * cnt
        cnt += 1

    print(cnt)
'''