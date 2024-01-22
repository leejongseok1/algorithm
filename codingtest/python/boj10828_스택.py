import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    operate = sys.stdin.readline().split()

    if operate[0] == 'push':
        stack.append(operate[1])

    elif operate[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    elif operate[0] == 'size':
        print(len(stack))
    
    elif operate[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    
    elif operate[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    
            