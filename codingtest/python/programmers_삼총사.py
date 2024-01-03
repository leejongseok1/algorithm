def solution(number):
    from itertools import combinations

    result = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            result += 1

    return result

def solution2(number):
    
    n = len(number)
    result = 0

    for i in range(len(number)):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if number[i] + number[j] + number[k] == 0:
                    result += 1
    
    return result
