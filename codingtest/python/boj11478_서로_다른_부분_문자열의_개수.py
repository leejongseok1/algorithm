import sys
input = sys.stdin.readline

s = input().strip()
result = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        result.add(s[i:j+1])
    
print(len(result))