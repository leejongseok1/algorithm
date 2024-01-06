def solution(strings, n):
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    answer = []

    for i in alpha:
        for j in range(len(strings)):
            if i == strings[j][n]:
                answer.append(strings[j])

    for i in range(len(answer)):
        for j in range(0, len(answer)-i-1):
            if answer[j][n] > answer[j+1][n] or (answer[j][n] == answer[j+1][n] and answer[j] > answer[j+1]):
                    answer[j], answer[j+1] = answer[j+1], answer[j]
    
    return answer

def solution2(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])