def solution(n, lost, reserve):
    
    # 차집합으로 공통요소 제거
    reserve1 = set(reserve) - set(lost)
    lost1 = set(lost) - set(reserve)
    
    for i in reserve1:
        if i-1 in lost1:
            lost1.remove(i-1)
        elif i+1 in lost1:
            lost1.remove(i+1)
    
    return n - len(lost1)

def solution2(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    # 원본 리스트 변경x
    # for i in reserve: 라면,
    # list index가 당겨져 원치않는 원소 삭제하는 문제 발생
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
            
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        if i+1 in lost:
            lost.remove(i+1)
            
    return n - len(lost)

n = 5
lost = [2, 4]
reserve = [1,3,5]

print(solution(n, lost, reserve))