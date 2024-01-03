def solution(k, score):
    answer = []
    rank = [] # 전당

    for i in score:
        if (len(rank) < k): # k번째 전까지는 명예의 전당에 추가
            rank.append(i)
        else:
            if (i > min(rank)): # 명예의 전당 최하위보다 현재 스코어가 높다면
                rank.remove(min(rank)) # 최하위 삭제하고
                rank.append(i)         # 현재 점수 추가
        
        rank.sort() # 오름차순 정렬
        answer.append(rank[0]) 

    return answer