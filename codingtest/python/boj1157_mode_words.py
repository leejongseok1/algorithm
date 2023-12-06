# 최빈 단어
str = input().upper()
str_list = list(set(str))

cnt_list = []

for i in str_list:
  cnt = str.count(i)
  cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
  print('?')
else:
  max_idx = cnt_list.index(max(cnt_list))
  print(str_list[max_idx])