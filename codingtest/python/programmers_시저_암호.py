def solution(s, n):
    
    result = ""    
    low_alpha = "abcdefghijklmnopqrstuvwxyz"
    upp_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for c in s:
        if c in low_alpha:
            idx = low_alpha.find(c) + n # c의 index를 찾아서 n 더함
            result += low_alpha[idx % 26]
        elif c in upp_alpha:
            idx = upp_alpha.find(c) + n
            result += upp_alpha[idx % 26]
        else:
            result += ' '
    
    return result