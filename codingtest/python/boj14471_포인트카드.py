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

n, m = map(int, input().split())

card = []
cnt = m - 1
temp = []
cost = 0

for _ in range(m):
    card.append(list(map(int, input().split())))

for i in range(len(card)):
    if card[i][0] < n: # 당첨 도장이 n개 미만이면
        temp.append(n-card[i][0])
    else:
        cnt -= 1

temp.sort() # 최솟값을 구하기 위해 정렬

if cnt > 0:
    for i in range(cnt): # cnt:얻고자하는 경품 갯수
        cost += temp[i]

print(cost)