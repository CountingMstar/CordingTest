from collections import deque, Counter
import sys

input = sys.stdin.readline
q = deque()

# n = 5
# stone = [1, 4, 2, 2, 1]
# start = 3
n = int(input())
stone = list(map(int, input().split()))
start = int(input())

indexs = [(i,n) for i, n in enumerate(stone)]
resurt = []

start = indexs[start-1]
resurt.append(start)

def new(indexs, cur):
    n1, n2 = 'nan', 'nan'
    ci, s = cur[0], cur[1]

    if (ci-s) >= 0 and (ci-s) < n:
        n1 = indexs[ci-s]
    if (ci+s) >= 0 and (ci+s) < n:
        n2 = indexs[ci+s]

    return n1, n2

q.append(start)

while True:
    last_q = str(q)

    for i in range(len(q)):
        cur = q.popleft()

        next_left, next_right = new(indexs, cur)

        if next_left != 'nan':
            q.append(next_left)
        if next_right != 'nan':
            q.append(next_right)

    for i in q:
        resurt.append(i)

    if last_q == str(q):
        break

resurt = Counter(resurt)
print(len(resurt))