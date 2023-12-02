n = int(input()) # 지불한 돈

n = 1000 - n # 거스름돈
cnt = 0 # 동전 갯수
coin_types = [500, 100, 50, 10, 5, 1]

for coin in coin_types:
    cnt += n // coin
    n %= coin

print(cnt)
    