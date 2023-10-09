from collections import deque
import sys
import itertools

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append([i, j])
        if graph[i][j] == 2:
            chicken.append([i, j])   
  
chicken_index = list(itertools.combinations([i for i in range(len(chicken))], M))

def chicken_distance(h, c):
    tmp = []
    hx, hy = h[0], h[1]
    for i in c:
        x, y = i[0], i[1]
        d = abs(x-hx) + abs(y-hy)
        tmp.append(d)
    return min(tmp)


distance = []
for i in chicken_index:
    d = 0
    c = []
    for j in i:
        c.append(chicken[j])
    for h in house:
        dis = chicken_distance(h, c)
        d += dis
    distance.append(d)

print(min(distance))
        

# a = [1,2,3,4,5]
# b = list(itertools.permutations(a, 2))
# c = list(itertools.combinations(a, 2))
# print(b)
# print(c)

