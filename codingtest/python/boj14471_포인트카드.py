'''
2n개의 도장 칸 / n개 이상 당첨이면 경품 교환
                1엔을 내고 꽝->당첨
   m - 1 개의 경품 가질 것임. 필요한 최솟값 구하라
   m : 포인트 카드 m장
입력 : n, m
      a, b 당첨, 꽝
4 5

1 7 // 3
6 2 ㅇ
3 5 // 1
4 4 ㅇ
0 8     '''
'''
n, m = map(int, input().split())

cnt = 0

for i in range(m):
    ao, bx = map(int, input().split())


while True:
    if ao >= n:
        continue
    elif ao < n:
        bx -= 1
        ao += 1
        cnt += 1
        if ao == 4:
            break
    
    if cnt == (m - 1):
        break

print(cnt)
'''


N,M = map(int, input().split(" "))
card = []
cnt = M-1
temp = []
cost = 0

for _ in range(M):
    card.append(list(map(int ,input().split(" "))))
    
for i in range(len(card)):
    if card[i][0] < N:
        temp.append(N-card[i][0])
    else:
        cnt -= 1
    
temp.sort()
    
if cnt > 0:
    for i in range(cnt):
        cost += temp[i]
            
print(cost)


    











