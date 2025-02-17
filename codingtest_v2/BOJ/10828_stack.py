import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    operate = sys.stdin.readline().split()
    
    if operate[0] == 'push':
        stack.append(int(operate[1]))
    
    elif operate[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    elif operate[0] == 'size':
        print(len(stack))
    
    elif operate[0] == 'empty':
        if stack:
            print(0)
        else: 
            print(1)
            
    elif operate[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)