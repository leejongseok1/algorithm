a0, a1 = map(int, input().split())
c = int(input())
n0 = int(input())

flag = 1
for i in range(n0, 100):
    if a0 * i + a1 > c * i:
        flag = 0
        break
print(flag)