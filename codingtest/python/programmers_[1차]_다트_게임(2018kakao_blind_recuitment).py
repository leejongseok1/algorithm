def solution(dartResult):
    
    result = [] 
    SDT = {
        'S' : 1,
        'D' : 2,
        'T' : 3,
    }
    cur_num = "" # 현재 숫자
    
    for dart in dartResult:
        
        # 숫자인 경우, 숫자를 추가
        if dart.isdigit():
            cur_num += dart
        
        # 보너스(S, D, T)인 경우, 점수를 계산해서 result에 추가
        elif dart in SDT:
            result.append(int(cur_num) ** SDT[dart])
            cur_num = ""
        
        # 스타상('*')인 경우, 최근 점수 2배
        elif dart == '*':
            result[-1] *= 2
            # 이전 점수도 2배
            if len(result) >= 2:
                result[-2] *= 2
        
        # 아차상('#')인 경우, 마지막 점수 음수
        elif dart == '#':
            result[-1] *= -1
            
    return sum(result)

dartResult1 = "1S2D*3T" # 1^1 * 2 + 2^2 * 2 + 3^3
dartResult2 = "1D#2S*3S" # 1^2 * (-1) * 2 + 2^1 * 2 + 3^1
print(solution(dartResult1))
print(solution(dartResult2))