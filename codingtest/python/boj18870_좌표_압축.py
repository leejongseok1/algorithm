import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

set_num = sorted(list(set(num)))
key = [i for i in range(len(set_num))]
num_dict = dict(zip(set_num, key))

for i in num:
    print(num_dict[i], end = ' ')