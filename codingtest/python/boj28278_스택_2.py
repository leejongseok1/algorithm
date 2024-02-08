import sys
input = sys.stdin.readline

stack = []
n = int(input())
for _ in range(n):
    command = list(map(int, input().split(' ')))
    
    if command[0] == 1: # add
        stack.append(command[1])
    elif command[0] == 2: # pop
        print(stack.pop(-1)) if stack else print(-1)
    elif command[0] == 3: # len
        print(len(stack))
    elif command[0] == 4: # empty
        print(0) if stack else print(1)
    elif command[0] == 5: # top
        print(stack[-1]) if stack else print(-1)