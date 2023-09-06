import sys

input = sys.stdin.readline
INF = int(1e9)

# num = 5
# relation = [(1,2),(2,3),(3,4),(4,5),(2,4),(5,3)]

relation = []
num = int(input())
while True:
    a,b = map(int, input().split())
    if a == -1 and b == -1:
        break
    relation.append([a,b])

tmp = 0
new_relation = []

for i, j in relation:
    if i > j:
        tmp = i
        i = j
        j = tmp
    new_relation.append([i,j,1])
    new_relation.append([j,i,1])

graph = [[INF]*(num+1) for i in range(num+1)]

for a in range(1, num+1):
    for b in range(1, num+1):
        if a == b:
            graph[a][b] = 0

for i in range(len(new_relation)):
    graph[new_relation[i][0]][new_relation[i][1]] = new_relation[i][2]

for k in range(1, num+1):
    for a in range(1, num+1):
        for b in range(1, num+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = []


for a in range(1, num+1):
    result.append(max(graph[a][1:]))
    # tmp = [0]
    # for b in graph[a]:
    #     if b != INF:
    #         tmp.append(b)
    # result.append(max(tmp))

r1 = []
r2 = []
r1.append(min(result))

for i, j in enumerate(result):
    if j == min(result):
        r2.append(i+1)

r1.append(len(r2))

a, b = '', ''
for i in r1:
    a += str(i)+' '
for i in r2:
    b += str(i)+' '

print(a)
print(b)











