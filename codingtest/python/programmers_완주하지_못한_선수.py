def solution(participant, completion):

    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    # completion를 다 돌아도 없을 경우 마지막 주자가 완주 실패 선수
    return participant[-1]

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

participant2 = ["mislav", "stanko", "mislav", "ana"]
completion2 = ["stanko", "ana", "mislav"]

print(solution(participant, completion))
print(solution(participant2, completion2))