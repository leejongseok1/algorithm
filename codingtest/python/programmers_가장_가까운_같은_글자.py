def solution(s):

    result = []
    s_dict = {}

    for i, word in enumerate(s):
        if word not in s_dict:
            result.append(-1)
            s_dict[word] = i
        else:
            result.append(i - s_dict[word])
            s_dict[word] = i

    return print(result)