import sys
input = sys.stdin.readline

n = int(input().strip())

string = []
for i in range(n):
    string.append(input().strip()) # 파일 이름 리스트에 저장

str_rule = list(string[0]) # 비교를 위해 첫번째값을 리스트로 저장
for i in range(n):
    for j in range(len(str_rule)):
        if str_rule[j] == string[i][j]: # 첫번째값과 나머지값 인덱스 별로 비교
            continue # 같으면 넘어감
        else:
            str_rule[j] = '?' # 다르면 '?'로 변환

print(''.join(str_rule))



# n = int(input().strip())
# first_str = list(input().strip())

# for i in range(n-1): # 위에서 first_word 입력받았으니 -1
#     other_str = list(input().strip())
#     for j in range(len(first_str)):
#         if first_str[j] != other_str[j]: # 인덱스 비교후 다르면
#             first_str[j] = '?' # 다른부분 '?'로 변환

# print(''.join(first_str))