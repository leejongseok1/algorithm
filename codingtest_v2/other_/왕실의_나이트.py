import sys
input_data = sys.stdin.readline().strip()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

can_steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

cnt = 0
for step in can_steps:
    next_row = row + step[0]
    next_col = col + step[1]
    
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        cnt += 1
        
print(cnt)