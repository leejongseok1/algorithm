import sys
input = sys.stdin.readline

while True:

    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    if a == b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    elif sum((a, b, c)) - max((a, b, c)) <= max((a, b, c)):
        print("Invalid")
    else:
        print("Scalene")