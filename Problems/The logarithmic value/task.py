import math

first = abs(int(input()))
second = int(input())

if second <= 0 or second == 1:
    print(round(math.log(first), 2))
else:
    print(round(math.log(first, second), 2))