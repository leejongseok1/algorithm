def solution(s):
    
    x_cnt = 0
    other_cnt = 0
    cnt = 0
    
    for i in s:
        if x_cnt == other_cnt:
            cnt += 1
            x = i
        if i == x:
            x_cnt += 1
        else:
            other_cnt += 1
    
    return cnt

print(solution('banana'))