from collections import deque
import sys
import itertools

N = input()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
aa = list(map(list,itertools.permutations(a,int(N))))

s = 1e9

for i in aa:
    tmp = 0
    for j in range(int(N)):
        tmp += i[j]*b[j]
    if s > tmp:
        s = tmp

print(s)





