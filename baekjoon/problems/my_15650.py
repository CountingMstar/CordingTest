from collections import deque
import sys, copy

input = sys.stdin.readline
N, M = map(int, input().split())
answer = []
total = []

def back():
    if len(answer) == M:
        ans = copy.deepcopy(answer)
        ans.sort()

        if ans not in total:
            total.append(ans)
        return 

    for i in range(1, N+1):
        if i not in answer:
            answer.append(i)
            back()
            answer.pop()

back()

print(total)
# print(set(total))
for t in total:
    print(" ".join(map(str, t)))