import sys
input = sys.stdin.readline

n = int(input())
print(int(n**0.5))

# 메모리초과로 실패 (n이 21억임)
# n = int(input())
#                         # n = 3
# windows = [0] * (n+1) # 0 0 0 0

# for i in range(1, n+1): # 2
#     for j in range(i, n+1, i): # 2 4 6
#         if windows[j] == 0:
#             windows[j] = 1
#         elif windows[j] == 1:
#             windows[j] = 0
            
# print(sum(windows))