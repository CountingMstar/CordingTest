import sys
from collections import Counter

INF = sys.maxsize
n1 = 3
g1 = [['a','b'],['b','c'],['c','d']]

alpha = []
for g in g1:
    if g[0] not in alpha:
        alpha.append(g[0])
    if g[1] not in alpha:
        alpha.append(g[1])
print('1111111111')
print(alpha)
num = len(alpha)

graph = [[INF]*(num+1) for i in range(num+1)]

for a in range(1,num+1):
    for b in range(1,num+1):
        if a == b:
            graph[a][b] = 0

for g in g1:
    g1, g2 = g[0], g[1]     
    graph[alpha.index(g1)][alpha.index(g2)] = 1
        
print(graph)

for k in range(1,num+1):
    for a in range(1,num+1):
        for b in range(1,num+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

print(graph)



