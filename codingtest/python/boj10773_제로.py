import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    num = int(input())
    if num != 0:
        stack.append(num)
    elif num == 0:
        stack.pop(-1)
        
print(sum(stack))