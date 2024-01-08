def eratosthenes(n):
    arr = [True for i in range(n + 1)]
    end = int(n**0.5) # n의 제곱근
    for i in range(2, end+1): # 2부터 n의 제곱근까지
        if arr[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 배수 제거
            j = 2 
            while i * j <= n:
                arr[i*j] = False
                j += 1

    for i in range(2, n+1):
        if arr[i]:
            print(i, end=' ')

print(eratosthenes(100))

def eratosthenes(n):
    arr = [i for i in range(n+1)]
    end = int(n**0.5) # n의 제곱근
    for i in range(2, end+1):
        # 소수가 아닌 수는 pass
        if arr[i] == 0:
            continue
        # 자기 자신 제외한 i의 배수 0으로 처리
        for j in range(i*i, n+1, i):
            arr[j] = 0
    
    return [i for i in arr[2:] if arr[i]]

print(eratosthenes(100))