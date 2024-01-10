def solution(a, b, c, d):

    dice = [a, b, c, d]
    dice_common = list(set(dice))
    
    # 4개 모두 같은 숫자일 때
    if len(dice_common) == 1:
        return int(str(dice_common[0]) * 4)
    
    elif len(dice_common) == 2:
        for i in dice_common:
            # 같은 숫자 3개, 다른 숫자 1개일 때
            if dice.count(i) == 3:
                p = i
                q = [x for x in dice_common if x != p][0]
                return pow((10 * p + q), 2)
            
            # 2개씩 같은 숫자일 때
            if dice.count(i) == 2:
                p = i
                q = [x for x in dice_common if x != p][0]
                return (p + q) * abs(p - q)
    
    # 같은 숫자 2개, 나머지 2개 각각 다른 숫자
    elif len(dice_common) == 3:
        for i in dice_common:
            if dice.count(i) == 2:
                qr = [x for x in dice_common if x != i]
                return qr[0] * qr[1]
    
    # 4개 모두 다를 때
    else:
        return min(dice)