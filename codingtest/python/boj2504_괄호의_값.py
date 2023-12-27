import sys
input = sys.stdin.readline

list = input().strip()

stack = []
result = 0
n = 1

for i in range(len(list)):
    
    if list[i] == "(":
        n *= 2
        stack.append(list[i])
    elif list[i] == "[":
        n *= 3
        stack.append(list[i])
    elif list[i] == ")":
        if not stack or stack[-1] != "(":
            result = 0
            break
        if list[i-1] == "(":
            result += n
        n //= 2
        stack.pop()
    elif list[i] == "]":
        if not stack or stack[-1] != "[":
            result = 0
            break
        if list[i-1] == "[":
            result += n
        
        stack.pop()
        n //= 3

if stack:
    print(0)
else:
    print(result)