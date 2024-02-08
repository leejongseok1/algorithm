import sys
T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    ps = input()
    for x in ps:
        if x == '(':
            stack.append(x) 
        elif x == ')':
            # 비어있지 않다면 pop으로 stack에 있는 '('를 지움 - 짝 OK
            if stack:
                stack.pop()
            else:
                # 비어있는데 ')'가 들어오면 VPS가 아닌 것.
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")

# ver 2

# import sys
# n = int(sys.stdin.readline())

# for _ in range(n):
#     ps = list(input())
#     sum = 0
#     for i in range(len(ps)):
#         if ps[i] == '(':
#             sum += 1
#         elif ps[i] == ')':
#             sum -= 1
    
#         if sum < 0:
#             print("NO")
#             break

#     if sum > 0: # 짝 안맞을 때
#         print("NO")
#     elif sum == 0:
#         print("YES")