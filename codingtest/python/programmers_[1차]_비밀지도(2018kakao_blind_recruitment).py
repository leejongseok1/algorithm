# 2018 KAKAO BLIND RECRUITMENT
def solution(n, arr1, arr2):

    result = []
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:].zfill(n)
        arr2[i] = bin(arr2[i])[2:].zfill(n)

        string = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                string += '#'
            else:
                string += ' '
    
        result.append(string)

    return result