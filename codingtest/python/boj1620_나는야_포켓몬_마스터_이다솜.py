import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

collection = [input().strip() for _ in range(n)] # 도감 Input
problem = [input().strip() for _ in range(m)]    # 문제 Input

num_dict = {str(k+1):v for k, v in enumerate(collection)} # key 번호 : value 이름
name_dict = {v:k+1 for k, v in enumerate(collection)}     # key 이름 : value 번호

for i in range(len(problem)):
    if problem[i] in num_dict:      # 포켓몬 번호가 문제여서 이름을 맞춰야할 때
        print(num_dict[problem[i]])
    elif problem[i] in name_dict:   # 포켓몬 이름이 문제여서 번호를 맞춰야할 때
        print(name_dict[problem[i]])