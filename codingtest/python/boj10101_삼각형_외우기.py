import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

sum = a + b + c

if a == 60 and b == 60 and c == 60:
    print("Equilateral")
elif sum == 180 and (a == b or a == c or b == c):
    print("Isosceles")
elif sum == 180 and (a != b or a != c or b != c):
    print("Scalene")
elif sum != 180:
    print("Error")
