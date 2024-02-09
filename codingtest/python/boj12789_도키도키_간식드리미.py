import sys
input = sys.stdin.readline

N = int(input())
line = list(map(int, input().split()))
space = []
target = 1
for i in line:
    space.append(i)
    while space and space[-1] == target:
        space.pop()
        target += 1
        
    if len(space) > 1 and space[-1] > space[-2]:
        print("Sad")
        break

else:
    print("Nice" if not space else "Sad")

# -------------------------------------
# N = int(input())
# line = list(map(int, input().strip().split()))
# space = []
# target = 1
# while line:
#     if line[0] == target:
#         line.pop(0)
#         target += 1
#     else:
#         space.append(line.pop(0))

#     while space:
#         if space[-1] == target:
#             space.pop()
#             target += 1
#         else:
#             break

# print("Nice" if not space else "NO")