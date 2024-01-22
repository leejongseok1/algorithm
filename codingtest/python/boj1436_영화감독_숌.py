# 1부터 10000까지 중 666이 들어간 수 찾기

import sys
input = sys.stdin.readline

N = int(input())
n = 666
cnt = 0

while True:
    if '666' in str(n): # n번째 수에 666 포함되어있다면
        cnt += 1        # cnt 증가
    if cnt == N:        # 카운트와 input N이 같다면
        print(n)        # n을 출력
        break           # while 종료
    n += 1              # n증가