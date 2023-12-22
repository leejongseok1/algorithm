import sys

a, b, v = map(int, sys.stdin.readline().strip().split())

day = (v - a) / (a - b) + 1 # 마지막날짜 +1

# 실수일 경우 1 더해줌
print(int(day) if day == int(day) else int(day) + 1)