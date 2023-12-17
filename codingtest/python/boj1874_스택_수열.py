import sys
input = sys.stdin.readline

n = int(input())

posb = True
op = []
stack = []
cnt = 1

for _ in range(n):
    data = int(input())

    # data(입력 숫자) 이하까지 stack에 push
    while cnt <= data:
        stack.append(cnt)
        op.append('+')
        cnt += 1
    
    # stack의 top과 data(입력 숫자)가 같다면 pop
    if stack[-1] == data:
        stack.pop()
        op.append('-')

    else:
        posb = False # 수열 생성 불가능
        break
# output
if posb == False:
    print("NO")
else:
    for i in op:
        print(i)