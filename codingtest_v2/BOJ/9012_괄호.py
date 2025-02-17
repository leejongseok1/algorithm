import sys
N = int(sys.stdin.readline())

for i in range(N):
    stack = []
    isValid = True
    op = sys.stdin.readline().strip()
    
    for j in range(len(op)):
        
        if op[j] == "(":
            stack.append(op[j])
            
        elif op[j] == ")":
            if not stack:
                print("NO")
                isValid = False
                break
            else:
                stack.pop()
    
    if isValid:    
        if stack:
            print("NO")
        else:
            print("YES")