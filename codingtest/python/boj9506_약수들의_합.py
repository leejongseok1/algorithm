import sys
input = sys.stdin.readline

while True:
    n = int(input())

    if n == -1:
        break

    div = []

    for i in range(1, n): # 자기자신 빼야하므로 n+1이 아닌 n까지
        if n % i == 0:
            div.append(i)
    
    if sum(div) == n:
        print(n,"=",end=" ")
        print(*div,sep=" + ") # unpacking
    else:
        print("%d is NOT perfect." %n)