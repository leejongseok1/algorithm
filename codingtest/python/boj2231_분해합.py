import sys
input = sys.stdin.readline

n = int(input())
Tag = False

for i in range(1, n+1):
    
    i1 = i // 1000000
    i2 = i // 100000 % 10
    i3 = i // 10000 % 10
    i4 = i // 1000 % 10
    i5 = i // 100 % 10
    i6 = i // 10 % 10
    i7 = i % 10

    sum = i + i1 + i2 + i3 + i4 + i5 + i6 + i7
    if sum == n:
        Tag = True
        print(i)
        break

if Tag == False:
    print(0)


# solution
'''
import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    num = sum((map(int, str(i))))
    sum0 = i + num

    if sum0 == n:
        print(i)
        break
    if i == n:
        print(0)
'''