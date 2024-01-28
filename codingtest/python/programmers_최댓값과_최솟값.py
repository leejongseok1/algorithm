def solution(s):
    
    num = list(map(int, s.split(' ')))
    return str(min(num)) + ' ' + str(max(num))

s = "-1 -2 -3 -4"
print(solution(s))