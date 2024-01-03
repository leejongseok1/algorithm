def solution(numbers):
    from itertools import combinations
    
    answer = []
    for i in combinations(numbers, 2):
        if sum(i) not in answer:
            answer.append(sum(i))
    
    return sorted(answer)