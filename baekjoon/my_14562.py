from collections import deque
import sys

S, T = 10, 20

input = sys.stdin.readline
st = []

n = int(input())
for i in range(n):
    S, T = map(int, input().split())
    st.append((S,T))

count = 0
final_count = 0

def next_step(cur):
    s, t = cur[0], cur[1]
    a = (2*s,t+3)
    b = (s+1,t)
    return a, b

def bfs(node, count):
    q = deque()
    q.append(node)
    final = False

    while q:
        count += 1
        for i in range(len(q)):
            tmp = q.popleft()
            a, b = next_step(tmp)

            if a[0] == a[1] or b[0] == b[1]:
                final = True
                final_count = count

            q.append(a)
            q.append(b)

        if final == True:
            break

    return final_count

for i in range(n):
    resurt = bfs(node=st[i], count=count)
    print(resurt)
