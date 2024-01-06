def solution(nums):
    result = len(set(nums))
    if result > len(nums)/2:
        return len(nums)/2
    return result

# 너무 어렵게 생각한 듯. 시간초과
def solution2(nums):
    from itertools import combinations

    monster = [list(set(i)) for i in set(list(combinations(nums, int(len(nums)/2))))] 
    answer = [len(i) for i in monster]
    
    return max(answer)

nums = [3,3,3,2,2,4]
print(solution(nums))