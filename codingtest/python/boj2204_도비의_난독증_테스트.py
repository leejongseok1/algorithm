# 대소문자 구분 안하고 어떤 단어가 사전순으로 가장 앞서는지
import sys
input = sys.stdin.readline

while True:

    T = int(input())
    if T == 0:
        break
    word = []
    for _ in range(T):
        w = input()
        word.append([w.upper(), w])
        # word.append(input())
    # word.sort(key=str.lower)
    word.sort()
    print(word[0][1]) # print(word[0])
