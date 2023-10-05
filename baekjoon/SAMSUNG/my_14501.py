from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

table = []
for i in range(N):
    T,P = map(int, input().split())
    table.append([T,P])

# print(N)
# print(table)

def dfs(day):
    tmp = []
    q = deque()
    T, P = table[day][0], table[day][1]
    next_day = day + T
    money = P

    if next_day > N-1:
        # print('222222222')
        return tmp
    
    q.append([next_day, money])

    while q:
        Q = q.popleft()
        next_day, money = Q[0], Q[1]
        if next_day > N-1:
            tmp.append(money)

        else:
            for nd in range(next_day, N):
                if table[nd][0]+nd-1 <= N-1:
                    q.append([table[nd][0]+nd, table[nd][1]+money])
                #     print('44444444')
                #     print(nd)
                #     print(table[nd][0])
                #     print(money)
                elif table[nd][0]+nd-1 > N-1:
                    # print('3333333333')
                    # print(nd)
                    # print(table[nd][0])
                    # print(money)
                    tmp.append(money)

    return tmp


result = []
for d in range(N):
#     print('111111111111')
#     print(d)
    tmp = dfs(d)
    if len(tmp) > 0:
        result.append(max(tmp))
#     print(result)

# print(result)
print(max(result))
