from collections import deque
import sys

input = sys.stdin.readline

# A, K = 5, 10
# A, K = 7, 77
# A, K = 1111, 997651
A, K = map(int,input().split())

def a(x):
    return x+1

def b(x):
    return x*2

queue = deque()
queue.append(A)
count = 0
answer = 0

while True:
    count += 1
    L = len(queue)
    print(count)

    for _ in range(L):
        k = queue.popleft()
        aa, bb = a(k), b(k)

        if aa < K:    
            queue.append(aa)
            queue.append(bb)

        if aa == K or bb == K:
            answer = count

    print('333333333')
    print(len(queue))

    if answer != 0:
        print(answer)
        break

