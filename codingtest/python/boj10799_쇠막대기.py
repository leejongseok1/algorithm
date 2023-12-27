import sys
input = sys.stdin.readline

razer = input().strip()
stack = []
cnt = 0

for i in range(len(razer)):
    if razer[i] == "(":
        stack.append("(")
    else:
        if razer[i-1] == "(":
            stack.pop()
            cnt += len(stack)
    
        else:
            stack.pop()
            cnt += 1

print(cnt)