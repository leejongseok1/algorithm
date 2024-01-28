def solution(keymap, targets):

    result = []
    
    for word in targets:    # targets 한 단어씩 loop
        times = 0           # 키 누른 횟수 총합
        
        for c in word:      # 한 단어의 한 문자
            flag = False    # 목표 문자열 작성가능여부 판단
            time = 101
            
            for key in keymap:
                if c in key: # key안에 c가 존재하면
                    # key목록의 c index+1과 time 중 최소값으로 update
                    time = min(key.index(c)+1, time)
                    flag = True
                    
            if not flag:
                times = -1; 
                break
            
            times += time # c 누른 횟수를 총합에 더함
        
        result.append(times)
    
    return result

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD", "AABB"]

keymap2 = ["AGZ", "BSSS"]
targets2 = ["ASA", "BGZ"]
print(solution(keymap, targets))
print(solution(keymap2, targets2))