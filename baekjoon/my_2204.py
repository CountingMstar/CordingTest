from collections import deque
import sys
import itertools
import copy

# a = 'A'
# print(ord(a))
# print(ord('Z'))
# print(chr(65))

# alpha = [chr(i) for i in range(65,91)]
# print(alpha)

a = ['A', 'b']
b = a.index('b')
print(b)

while True:
    n = int(input())
    if n == 0:
        break
    original = [input() for i in range(n)]
    low = [i.lower() for i in original]
    low2 = copy.deepcopy(low)

    low.sort()
    first = low[0]
    ind = low2.index(first)
    print(original[ind])
    # print(original)
    # print(low)
    # tmp.sort()
    # print(tmp[0])







"""
3
Cat
fat
bAt
4
call
ball
All
Hall
0
"""