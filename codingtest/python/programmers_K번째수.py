def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        arrayi = array[i-1:j]
        arrayi.sort()
        answer.append(arrayi[k-1])
        
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))