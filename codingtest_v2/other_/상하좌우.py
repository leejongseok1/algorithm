import sys
n = int(sys.stdin.readline())
move = list(sys.stdin.readline().split())

raw = 1
col = 1
for i in range(len(move)):
    next_raw = raw
    next_col = col
    
    if move[i] == 'R':
        next_col += 1
    elif move[i] == 'L':
        next_col -= 1
    elif move[i] == 'U':
        next_raw -= 1
    elif move[i] == 'D':
        next_raw += 1
    
    if 1 <= next_col <= n and 1 <= next_raw <= n:
        raw = next_raw
        col = next_col
        
print(col, raw)
    
    