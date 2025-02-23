import sys
n = int(sys.stdin.readline())
move = list(sys.stdin.readline().split())

row = 1
col = 1
for i in range(len(move)):
    next_row = next_row
    next_col = col
    
    if move[i] == 'R':
        next_col += 1
    elif move[i] == 'L':
        next_col -= 1
    elif move[i] == 'U':
        next_row -= 1
    elif move[i] == 'D':
        next_row += 1
    
    if 1 <= next_col <= n and 1 <= next_row <= n:
        row = next_row
        col = next_col
        
print(row, col)