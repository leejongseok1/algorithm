def solution(players, callings):
    
    result = {player: i for i, player in enumerate(players)}
    
    for who in callings:
        i = result[who]
        result[who] -= 1
        result[players[i-1]] += 1
        players[i-1], players[i] = players[i], players[i-1]
        
    return players