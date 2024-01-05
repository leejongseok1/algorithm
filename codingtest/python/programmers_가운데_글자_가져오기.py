def solution(s):
    
    if len(s) % 2 != 0:
        return str(s[(len(s)//2)])
    
    elif len(s) % 2 == 0:
        return str(s[len(s)//2-1]) + str(s[len(s)//2])