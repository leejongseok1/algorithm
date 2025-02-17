import sys
n = int(sys.stdin.readline())
num = [int(sys.stdin.readline().strip())]

stack = []
op = []
num_idx = 0

for i in range(1, n+1):
    stack.append(i)
    op.append('+')
    
    while stack and stack[-1] == num[num_idx]:
        stack.pop()
        op.append('-')
        num_idx += 1
        
    if num_idx == n:
        break
    
if num_idx != n:
    print("NO")
else:
    for i in op:
        print(i)