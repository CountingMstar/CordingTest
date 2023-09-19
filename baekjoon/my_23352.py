from collections import deque
import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

def bfs(graph,x,y):
    q = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    count = 1
    start = graph[x][y]
    q.append([x,y,count,start])
    
    result = []
    
    while q:
        if len(q) == 0:
            break

        x,y,count,score = q.popleft()
        check = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1 or graph[nx][ny] == 0:
                check += 1
                continue

            if graph[nx][ny] != 0:
                count += 1
                q.append([nx,ny,count,graph[nx][ny]])
                graph[nx][ny] = 0

        if check == 4:
            end = score
            result.append([start,end,count])

    if len(result) == 0:
        return 0

    final_start, final_end, final_count = 0, 0, 0
    for i in range(len(result)):
        start = result[i][0]
        end = result[i][1]
        count = result[i][2]

        if final_count < count:
            final_count = count
            final_start = start
            final_end = end

        elif final_count == count:
            final_sum = final_start + final_end
            new_sum = start + end

            if final_sum < new_sum:
                final_count = count
                final_start = start
                final_end = end
    print('========')
    print(count)
    return (count, final_start + final_end)

final_count, final_result = 0, 0
for x in range(N):
    for y in range(M):
        graph2 = copy.deepcopy(graph)

        if graph2[x][y] != 0:
            # final_result.append(bfs(graph2,x,y))
            count, final = bfs(graph2,x,y)
            print('######')
            print(count)
            print(final)
            if final_count < count:
                final_count = count
                final_result = final

            elif final_count == count:
                if final_result < final:
                    final_result = final

            print(final_count)
            print(final_result)

print(final_count)
print(final_result)
