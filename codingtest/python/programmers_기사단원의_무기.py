# solution 2,3,4 정답
# 첫번째 시도 시간초과
def solution1(number, limit, power):
    
    divisor = [0] * (number+1)
    for knight in range(1, number+1):
        for j in range(1, knight+1):
            if knight % j == 0:
                divisor[knight] += 1
                
    for div in range(len(divisor)):
        if divisor[div] > limit:
            divisor[div] = power
    
    return sum(divisor)

def solution2(number, limit, power): # 왜 되는지 모르겠음;
    
    divisor = [1] * (number+1)
    
    for knight in range(2, number+1):
        for j in range(knight, number+1, knight):
            divisor[j] += 1
            
    for div in range(1, number + 1):
        if divisor[div] > limit:
            divisor[div] = power

    return sum(divisor)-1 

def solution3(number, limit, power):
    divisor = [0] * (number + 1)

    for knight in range(1, number + 1):
        
        for j in range(1, int(knight**0.5) + 1):
            if knight % j == 0: # 
                divisor[knight] += 2  
                if j == knight // j:
                    divisor[knight] -= 1

    for div in range(1, number + 1):
        if divisor[div] > limit:
            divisor[div] = power

    return sum(divisor)

def solution4(number, limit, power):
    divisor = [] # 약수 list
    for knight in range(1, number+1): # 기사번호
        div = 0
        for j in range(1, int(knight**0.5)+1): # 1부터 기사번호 제곱근까지 loof
            if knight % j == 0: # 약수라면 증가 
                div += 1
                if j**2 != knight: # 제곱이 되는 수는 1더해 중복 방지
                    div += 1
            if div > limit:
                div = power
                break
        divisor.append(div)
    return sum(divisor)