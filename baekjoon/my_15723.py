import sys
from collections import Counter
from string import ascii_lowercase

# INF = sys.maxsize
INF = int(1e9)
# n1 = 3
# G1 = [['a','b'],['b','c'],['c','d']]
# n2 = 3
# G2 = [['a','d'],['a','c'],['d','a']]

input = sys.stdin.readline
alpha = list(ascii_lowercase)
num = len(alpha)
graph = [[INF]*(num+1) for i in range(num+1)]

n1 = int(input())
for i in range(n1):
    G = str(input())
    g1, g2 = G[0], G[-2]
    graph[alpha.index(g1)+1][alpha.index(g2)+1] = 1


for k in range(1,num+1):
    for a in range(1,num+1):
        for b in range(1,num+1):
            if a == b:
                graph[a][b] = 0
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


n2 = int(input())
for g in range(n2):
    G = str(input())
    g1, g2 = G[0], G[-2]
    if graph[alpha.index(g1)+1][alpha.index(g2)+1] == INF:
        print('F')
    else:
        print('T')
