def solution(s, skip, index):
    result = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    f_alpha = '' # skip 제외한 알파벳 (filter_alphabet)
    for c in alphabet:
        if c not in skip:
            f_alpha += c
    
    # for c in list(skip):
    #     alphabet = alphabet.replace(i,"")
    
    for c in s:
        result += f_alpha[(f_alpha.find(c) + index) % len(f_alpha)]
        
    return result


s = "aukks"
skip = "wbqd"
index = 5
print(solution(s, skip, index))