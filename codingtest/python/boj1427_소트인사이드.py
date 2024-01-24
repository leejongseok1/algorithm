import sys
input = sys.stdin.readline

n = int(input())

num = []
for i in str(n):
    num.append(int(i)) # num = list(map(int, str(n)))
    
num.sort(reverse=True)

for i in num:
    print(i, end='')