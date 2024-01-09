def solution(babbling):
    
    result = 0
    babb_can = ['aya', 'ye', 'woo', 'ma']
    for i in babbling:
        for j in babb_can:
            if j * 2 not in i:
                i = i.replace(j,' ')

        if len(i.strip()) == 0:
            result += 1
    
    return result

def solution2(babbling):
    
    result = 0
    babb_can = ['aya', 'ye', 'woo', 'ma']
    repeats = ['ayaaya', 'yeye', 'woowoo', 'mama']
    
    for babb in babbling:
        for rep in repeats:
            babb = babb.replace(rep, 'X')
        for can in babb_can:
            babb = babb.replace(can, 'O')
            
        isValid = True
        for c in babb:
            if c != 'O':
                isValid = False
                break
        if isValid == True:
            result += 1

    return result

babbling = ["aya", "yee", "u", "maa"]
babbling2 = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling2))
print(solution2(babbling2))