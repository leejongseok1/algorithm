import sys
input = sys.stdin.readline

n = int(input())

result = []
for _ in range(n):
    [x, y] = map(int, input().split())
    result.append([x, y])
    
result.sort()
for i in result:
    print(i[0], i[1])
    
# sort()는 2차원 배열에 대해 기본적으로 앞에 있는 요소부터 정렬하기 때문에
# 그냥 sort() 후 print 하면 됨.