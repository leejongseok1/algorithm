matrix = []

for _ in range(9):
  row = list(map(int, input().split()))
  matrix.append(row)
  
max_num = -10001
for i in range(9):
  big = max(matrix[i])
  if big > max_num:
    max_num = big
    row_idx = i + 1
    col_idx = matrix[i].index(big) + 1
    
print(max_num)
print(row_idx, col_idx)