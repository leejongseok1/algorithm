def solution(s, n):
    
    alpha_low = 'abcdefghijklmnopqrstuvwxyz'
    alpha_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    answer = ''
    
    for char in s:
        if char in alpha_low:
            idx = alpha_low.find(char) + n
            answer += alpha_low[idx%26]
        elif char in alpha_up:
            idx = alpha_up.find(char) + n
            answer += alpha_up[idx%26]
        else:
            answer += ' '
    
    return answer