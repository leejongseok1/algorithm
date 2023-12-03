t = int(input())

for _ in range(t):
    n = int(input())
    temp = [i for i in range(1, n+1)]
    testcase = list(map(int, input().split()))


    for i in range(len(temp)):
        if temp[i] == testcase[i]:
            temp[i] += 1
        
        for j in range(i+1, len(temp)):
            if temp[j-1] >= temp[j]:
                temp[j] += (temp[j-1] - temp[j]) + 1


    print(temp[-1])