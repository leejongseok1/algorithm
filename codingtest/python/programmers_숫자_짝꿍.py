def solution(X, Y):
    from collections import Counter
    answer = ''
    
    # 각 숫자 발생 횟수 계산
    cnt_X, cnt_Y = Counter(X), Counter(Y)
    
    # 내림차순
    common = sorted(cnt_X & cnt_Y, reverse = True)
    
    # 공통된 숫자가 없다면 '-1' 반환
    if not common:
        return '-1'
    
    # 짝 지을 수 있는 공통 숫자 수 만큼 곱해서 문자열 만듦
    for i in common:
        answer += str(i * min(cnt_X[i], cnt_Y[i]))
    
    # 문자열이 0으로만 이루어진 경우 '0' 반환
    if len(answer) == answer.count('0'):
        return '0'
    else:
        return answer

X = "100"
Y = "2345" # -1 

X2 = "100"
Y2 = "203045" # 0

X3 = "5525" 
Y3 = "1255" # 552

print(solution(X, Y))
print(solution(X2, Y2))
print(solution(X3, Y3))

# 9 ~ 0 순으로 숫자를 조회하면서 answer의 성분이 내림차순으로 더해짐
def solution2(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer