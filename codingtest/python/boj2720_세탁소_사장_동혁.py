'''
리암이 줘야할
쿼터(0.25) , 다임(0.10) , 니켈(0.05) , 페니(0.01)의 개수를 구하라
거스름돈은 항상 5달러 이하이고
손님이 받는 동전의 개수는 최소화.
'''
# 124센트 - 1.24달러 - 쿼터4개, 다임2개, 니켈0개, 페니4개

import sys
input = sys.stdin.readline

T = int(input())

coin_type = [25, 10, 5, 1]

for _ in range(T):
    change = int(input())

    for coin in coin_type:
        print(change // coin, end=' ')
        change = change % coin