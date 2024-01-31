import sys
input = sys.stdin.readline

n = int(input())
words = []
for _ in range(n):
    words.append(input().strip())
# --- 
set_words = []
for word in words:
    if word not in set_words:
        set_words.append(word)
        
set_words.sort()   
set_words.sort(key=len)
for i in set_words:
    print(i)


# set_words = set(words)
# words = list(set_words)
# words.sort()
# words.sort(key=len)
# for i in words:
#     print(i)