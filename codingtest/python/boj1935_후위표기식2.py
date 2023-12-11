import sys

n = int(sys.stdin.readline().strip()) # 피연산자 갯수
expression = sys.stdin.readline().strip() # 후위표기식
num = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
for word in expression:
    if word.isalpha():
        stack.append(num[ord(word) - ord('A')])
    else:
        num2 = stack.pop()
        num1 = stack.pop()

        if word == '+':
            stack.append(num1 + num2)
        elif word == '-':
            stack.append(num1 - num2)
        elif word == '*':
            stack.append(num1 * num2)
        elif word == '/':
            stack.append(num1 / num2)

print('%.2f' % stack[0])