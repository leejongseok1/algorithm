def solution(name, yearning, photo):
    
    dict1 = dict(zip(name, yearning))

    result = []
    
    for i in photo:
        score = 0
        for j in i:
            if j in dict1:
                score += dict1[j]
        result.append(score)
        
    return result

# ㄷㄷ
# def solution(name, yearning, photo):
#     return [sum(yearning[name.index(j)] for j in i if j in name) for i in photo]