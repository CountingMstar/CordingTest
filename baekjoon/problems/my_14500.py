from collections import deque
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]

def fig(x,y,type):
    f = [[[x,y],[x,y+1],[x,y+2],[x,y+3]],
        [[x,y],[x+1,y],[x+2,y],[x+3,y]],
        [[x,y],[x,y+1],[x+1,y],[x+1,y+1]],
        [[x,y],[x,y+1],[x+1,y],[x+1,y+1],[x+2,y],[x+2,y+1]],
        [[x,y],[x,y+1],[x,y+2],[x+1,y],[x+1,y+1],[x+1,y+2]]]
    return f[type]

t3 = [[0,2,4,5],[1,3,4,5],[0,1,2,4],[0,1,3,5],[0,2,3,5],[1,2,3,4],[0,2,3,4],[1,2,3,5],[0,1,2,3],[0,1,2,5],[0,3,4,5],[2,3,4,5]]
t4 = [[1,2,3,4],[0,1,4,5],[0,1,2,4],[1,3,4,5]]
result = []

for i in range(N):
    for j in range(M):
        for t in range(5):
            F = fig(i,j,t)

            if t < 3:
                r = 0
                for k in F:
                    if k[0] > N-1 or k[1] > M-1:
                        continue
                    r += graph[k[0]][k[1]]
                result.append(r)

            elif t == 3:
                for tt in t3:
                    r = 0
                    for ttt in tt:
                        if F[ttt][0] > N-1 or F[ttt][1] > M-1:
                            continue
                        r += graph[F[ttt][0]][F[ttt][1]]
                    result.append(r)

            elif t == 4:
                for tt in t4:
                    r = 0
                    for ttt in tt:
                        if F[ttt][0] > N-1 or F[ttt][1] > M-1:
                            continue
                        r += graph[F[ttt][0]][F[ttt][1]]
                    result.append(r)

print(max(result))