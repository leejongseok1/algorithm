    # 페인트가 칠해진 n미터 벽
    # 1미터 구역 n개로 나눔
    # 롤러의 길이 m미터
    # section을 m미터인 롤러로 몇번 칠해서 다 칠할 수 있는가

# 정답
def solution(n, m, section):
    roller = 1 # 롤러 횟수
    paint = section[0] # 덧칠 시작점
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            roller += 1
            paint = section[i]
    
    return  roller

# 첫번째 시도. 정확성 테스트 실패
def solution1(n, m, section):
    
    paint = [1] * n
    roller = 0
    for i in section:
        paint[i-1] = 0
    
    for i in range(len(paint)):
        if paint[i] == 0:
            start = max(0, i - (m//2)) # 덧칠 시작점
            end = min(n, i + (m//2) + 1) #    끝점
            paint[start: end] = [1] * (end - start)
            roller += 1
    
    return roller

n, m = 8, 4
section = [2, 3, 6]
print(solution(n, m, section))