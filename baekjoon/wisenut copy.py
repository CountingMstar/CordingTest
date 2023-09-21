from collections import Counter
X = 'b'

relation = [['a','b'],['a','c'],['a','d'],['b','e'],['e','d']]

tmp = []
for i, j in relation:
    if i == X:
        tmp.append(j)
    if j == X:
        tmp.append(i)

tmp2 = []
for t in tmp:
    for i, j in relation:
        if i == t:
            tmp2.append(j)
        if j == t:
            tmp2.append(i)  

a = Counter(tmp2)
a[X] = 0
k = list(a.keys())
v = list(a.values())

for i in range(len(v)):
    if v[i] == max(v):
        print(k[i])





# INF = 1e9
# r = []
# for i in relation:
#     r.append(i[0])
#     r.append(i[1])

# print(r) 
# people = sorted(list(set(r)))
# print(people)
# N = len(people)
# graph = [[INF]*N for i in range(N)]
# print(graph)