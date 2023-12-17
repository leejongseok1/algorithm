''' 2:10 시작
1~N : N개의 풍선 원형
i 오른쪽 i + 1 왼쪽 i - 1
풍선에는 종이 있음.  -N <= 종이숫자 <= N
1번 풍선 터뜨린 뒤 종이숫자만큼 이동하여 터뜨림

 paper_num (input)// remove (output)
3, 2, 1, -3, -1 // 1, 4, 5, 3, 2
'''
# input : 풍선 갯수 , N개 풍선 안의 종이 숫자
# ouput : 터진 풍선의 번호. 순서대로

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

paper = deque(list(map(int, input().rstrip().split()))) # 종이 숫자
ballon_idx = deque([i for i in range(1, n+1)]) # 풍선 번호

while paper:
    i = paper[0]
    if i > 0:
        paper.popleft()
        paper.rotate(-i + 1)
        print(ballon_idx.popleft())
        ballon_idx.rotate(-i+1)
    else: # i < 0
        paper.popleft()
        paper.rotate(-i) # -(-paper) -> 양수가 됨
        print(ballon_idx.popleft())
        ballon_idx.rotate(-i)