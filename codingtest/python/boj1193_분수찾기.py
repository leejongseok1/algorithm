import sys
n = int(sys.stdin.readline())

line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 1: # 홀수 일 때
    a = line - n + 1
    b = n
elif line % 2 == 0: # 짝수 일 때
    a = n
    b = line - n + 1

print(f'{a}/{b}')