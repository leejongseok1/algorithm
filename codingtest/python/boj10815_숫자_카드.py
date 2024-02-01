import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

card_dict = {cards[i]: 0 for i in range(len(cards))}

for i in range(M):
    if checks[i] in card_dict:
        print('1', end=' ')
    else:
        print('0', end=' ')