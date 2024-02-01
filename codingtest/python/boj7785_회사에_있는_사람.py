import sys
input = sys.stdin.readline

n = int(input())    
log = dict()
for _ in range(n):
    name, commute = map(str, input().split())
    
    if commute == "enter":
        log[name] = commute
    else:
        log.pop(name)
        
log = sorted(log.keys(), reverse=True)

for i in log:
    print(i)

# n = int(input())
# log = []
# for _ in range(n):
#     log.append(input().split())

# dict_log = {log[i][0] : log[i][1] for i in range(len(log))}
    
# remove = []
# for key, value in dict_log.items():
#     if value == 'leave':
#         remove.append(key)
        
# for key in remove:
#     dict_log.pop(key)
    
# log = sorted(list(dict_log), reverse=True)

# for i in log:
#     print(i)