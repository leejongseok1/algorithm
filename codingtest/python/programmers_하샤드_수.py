def solution(x):
    
    i1 = x // 10000 % 10
    i2 = x // 1000 % 10
    i3 = x // 100 % 10
    i4 = x // 10 % 10
    i5 = x % 10 
    
    sum = i1 + i2 + i3 + i4 + i5
    
    if x % sum == 0:
        return True
    else:
        return False