def solution(lottos, win_nums):

    rank_dict = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    
    max_score = 0
    min_score = 0
    
    for lotto in lottos:
        for win in win_nums:
            if lotto == win:
                max_score += 1
                min_score += 1
        if lotto == 0:
            max_score += 1
    
    return [rank_dict[max_score], rank_dict[min_score]]

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))