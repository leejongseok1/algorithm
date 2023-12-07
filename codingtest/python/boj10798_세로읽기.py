in_words = []

for _ in range(5):
    s = input()
    in_words.append(s)

for i in range(max(len(w) for w in in_words)):
    for j in range(len(in_words)):
        if i < len(in_words[j]):
            print(in_words[j][i], end='')