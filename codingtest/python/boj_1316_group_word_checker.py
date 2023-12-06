n = int(input())

cnt_group = 0
for _ in range(n):
    word = input()
    check = 0
    for i in range(len(word)-1):
      if word[i] != word[i+1]:
        new_word = word[i+1:]
        if new_word.count(word[i]) > 0:
          check += 1

    if check == 0:
      cnt_group += 1
print(cnt_group)
    

