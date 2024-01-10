def solution(a, b, c, d):

    dice = [a, b, c, d]
    dice_common = list(set(dice))
    
    if len(dice_common) == 1:
        return int(str(dice_common[0]) * 4)
    
    elif len(dice_common) == 2:
        for i in dice_common:
            if dice.count(i) == 3:
                p = i
                q = [x for x in dice_common if x != p][0]
                return pow((10 * p + q), 2)
            
            if dice.count(i) == 2:
                p = i
                q = [x for x in dice_common if x != p][0]
                return (p + q) * abs(p - q)
    
    elif len(dice_common) == 3:
        for i in dice_common:
            if dice.count(i) == 2:
                qr = [x for x in dice_common if x != i]
                return qr[0] * qr[1]
    
    else:
        return min(dice)