def solution(k, m, score):
    
    benefit = 0
    
    score.sort(reverse=True)

    for i in range(0, len(score), m):
        if len(score[i:i+m]) == m:
            benefit += min(score[i:i+m]) * m
    
    return benefit