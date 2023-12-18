import sys
n = int(sys.stdin.readline())

line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 1: # 홀수 일 때
    top = line - n + 1
    bottom = n
elif line % 2 == 0: # 짝수 일 때
    top = n
    bottom = line - n + 1

print(top, '/', bottom, sep="")

# print(f'{top}/{bottom}')  -> 시간초과