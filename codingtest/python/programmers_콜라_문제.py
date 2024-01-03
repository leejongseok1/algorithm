def solution(a, b, n):
        #    2  1  20 = 19
        #    3  2  20 = 
    result = 0

    while n >= a:

        remain_coke = n % a
        n = (n // a) * b
        result += n
        n += remain_coke
 
    return result

solution(2, 1, 20)