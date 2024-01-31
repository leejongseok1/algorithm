import sys
input = sys.stdin.readline

n = int(input())
users = []
for _ in range(n):
    [age, name] = input().split()
    users.append([int(age), name])
    
users.sort(key=lambda x:x[0]) # x[0] (age)만 비교하여 sort

for i in users:
    print(i[0], i[1])