def solution(N, stages):
    
    people = len(stages) # 도전자
    fail_rate = []       # 실패율
    for i in range(1, N+1): # 스테이지마다 loop
        stage_fail = 0 # 스테이지에 도달했으나 클리어하지 못한 player 수
        for j in range(len(stages)): # 도전자 수 만큼 loop
            if stages[j] == i: # i 스테이지 클리어하지 못한 player 수
                stage_fail += 1 
        if stage_fail == 0: 
            fail_rate.append(0) # 클리어 한 player와 도달하지 못한 player만 있을 때
        else:
            fail_rate.append(stage_fail / people) # 실패율 계산 후 append
        people -= stage_fail # 도전자수 -= 클리어하지 못한 player 수
            # enumerate를 사용해 실패율을 기준으로 내림차순 정렬
    result = [i[0]+1 for i in sorted(enumerate(fail_rate), key=lambda x: x[1], reverse=True)]
    
    return result

def solution2(N, stages):

    people = len(stages)
    fail_rate = {}
    for i in range(1, N+1):
        if people != 0:
            fail_rate[i] = stages.count(i) / people
            people -= stages.count(i)
        else:
            fail_rate[i] = 0

    return sorted(fail_rate, key=lambda i: fail_rate[i], reverse=True)

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
print(solution2(N, stages))