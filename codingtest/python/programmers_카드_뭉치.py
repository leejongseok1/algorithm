def solution(cards1, cards2, goal):
    answer = []
    n = len(cards1)
    m = len(cards2)

    i = j = 0

    for word in goal:
        if i < len(cards1) and word == cards1[i]:
            answer.append(cards1[i])
            i += 1
        if j < len(cards2) and word == cards2[j]:
            answer.append(cards2[j])
            j += 1
    
    if answer == goal:
        return 'Yes'
    else:
        return 'No'

from collections import deque

def solution2(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards1)

    for word in goal:
        if cards1 and word == cards1[0]: cards1.popleft()
        if cards2 and word == cards2[0]: cards2.popleft()
        else: return 'No'

    return 'Yes'