def solution(nums):
    from itertools import combinations
    num_list = [sum(i) for i in combinations(nums, 3)]
    cnt = 0
    for num in num_list:
        if is_prime(num):
            cnt += 1
        else: continue

    return cnt
    
def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

nums = [1, 2, 3, 4]
nums2 = [1, 2, 7, 6, 4]
print(solution(nums))
print(solution(nums2))