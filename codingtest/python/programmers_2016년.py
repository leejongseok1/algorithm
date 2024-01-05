def solution(a, b):
    
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = 0
    for i in range(a-1):
        answer += months[i]
    
    answer += b
    answer %= 7
    
    return days[answer-1]