from collections import deque
import sys

input = sys.stdin.readline
N, M, X, Y, K = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]
order = list(map(int, input().split()))

jusawi = [[0] for i in range(6)]

def direction(jusawi,d,x,y):
    tmp = []
    # 동 서 북 남
    if d == 1:
        I = [4,2,1,6,5,3]
        nx, ny = x, y+1
    if d == 2:
        I = [3,2,6,1,5,4]
        nx, ny = x, y-1
    if d == 3:
        I = [5,1,3,4,6,2]
        nx, ny = x-1, y
    if d == 4:
        I = [2,6,3,4,1,5]
        nx, ny = x+1, y

    if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
        return jusawi,x,y,False

    for i in I:
        tmp.append(jusawi[i-1])

    if tmp[-1][0] != 0 and graph[nx][ny] == 0:
        graph[nx][ny] = tmp[-1][0]

    elif graph[nx][ny] != 0:
        tmp[-1][0] = graph[nx][ny]
        graph[nx][ny] = 0

    jusawi = tmp
    return jusawi,nx,ny,True


for d in order:
    jusawi,X,Y,TF = direction(jusawi,d,X,Y)
    if TF:
        print(jusawi[0][0])


