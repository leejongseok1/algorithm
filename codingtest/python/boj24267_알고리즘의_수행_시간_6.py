n = int(input())

ans = 0
for i in range(1, n - 1):
    ans += (n - (i + 1)) * (n - i) // 2
print(ans)
print(3)