X = ''

relation = [['a','b'],['a','c'],['a','d'],['b','e'],['e','d']]

INF = 1e9
r = []
for i in relation:
    r.append(i[0])
    r.append(i[1])

print(r) 
people = sorted(list(set(r)))
print(people)
N = len(people)
graph = [[INF]*N for i in range(N)]
print(graph)

for a in range(N):
    for b in range(N):
        if a == b:
            graph[a][b] = 0
        
for i, j in relation:
    a = people.index(i)
    b = people.index(j)
    graph[a][b] = 1
    graph[b][a] = 1

graph2 = [[0]*N for i in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

print(graph)

