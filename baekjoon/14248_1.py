from collections import deque
import sys

input = sys.stdin.readline

# n = int(input())
# graph = list(map(int, input().split()))
# s = int(input)-1
n = 5
graph = [1, 4, 2, 2, 1]
s = 3-1

check = [0]*n
print(check)

def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 1

    while q:
        node = q.popleft()

        for d in [-graph[node], graph[node]]:
            print(d)
            t = node+d

            if (0 <= t < n) and check[t] == 0:
                q.append(t)
                check[t] = 1

bfs(s)
print(check.count(1))
