from collections import deque
import copy

relation = [(1,2),(2,3),(3,4),(4,5),(2,4),(5,3)]
num = 5

def bfs(s, c):
    q = deque()
    data = (s,c)
    q.append(data)

    while True:
        s,c = q.popleft()
        tmp = []

        for i in relation:
            i1, i2 = i[0], i[1]

            if s == i1:
                q.append((i2,c+1))
                tmp.append(i)
            elif s == i2:
                q.append((i1,c+1))
                tmp.append(i)

        for t in tmp:
            relation.remove(t)

        if len(relation) == 0:
            score = q[0][1]
            break

    return score

scores = []        

for i in range(1, num+1):
    relation2 = copy.deepcopy(relation)
    score = bfs(s=i,c=0)
    scores.append(score)
    relation = copy.deepcopy(relation2)

print(scores)
print(scores.index(min(scores)))





