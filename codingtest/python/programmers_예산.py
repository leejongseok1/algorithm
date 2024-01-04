def solution(d, budget):
    
    d.sort()
    cnt = 0
    num_sum = 0
    for i in range(len(d)):
        num_sum += d[i]
        if num_sum > budget:
            cnt = i
            break

    if num_sum <= budget:
        cnt = len(d)
        
    return cnt