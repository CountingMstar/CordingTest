myGraph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J'],
    'G': ['C'],
    'H': ['D'],
    'I': ['E'],
    'J': ['F']
}


"""
BFS(Breath-First Search)
"""

def my_bfs(graph, start_node):
    visited = list() # 방문한 노드를 담을 배열
    queue = list() # 방문 예정인 노드를 담을 배열

    queue.append(start_node) # 처음에는 시작 노드 담아주고 시작하기.
    print('11111111')
    print(queue)

    while queue: # 더 이상 방문할 노드가 없을 때까지.
        node = queue.pop(0) # 방문할 노드를 앞에서 부터 하나싹 꺼내기.
        print('222222222')
        print(queue)

        if node not in visited: # 방문한 노드가 아니라면
            visited.append(node) # visited 배열에 추가
            queue.extend(graph[node]) # 해당 노드의 자식 노드로 추가

            print('3333333')
            print(node)
            print(visited)
            print(graph[node])
            print(queue)
    
    print("bfs - ", visited)
    return visited
    
# 함수 실행
my_bfs(myGraph, 'A')



# """
# DFS(Depth-First Search)
# """

# def my_dfs(graph, start_node):
#     visited = list() # 방문한 노드를 담을 배열
#     stack = list() # 정점과 인접한 방문 예정인 노드를 담을 배열

#     stack.append(start_node) # 처음에는 시작 노드 담아주고 시작하기.
#     print('11111111')
#     print(stack)

#     while stack: # 더 이상 방문할 노드가 없을 때까지.
#         print('222222222')
#         print(stack)

#         node = stack.pop() # 방문할 노드를 앞에서 부터 하나싹 꺼내기.
#         print('333333')
#         print(node)

#         if node not in visited: # 방문한 노드가 아니라면
#             print('888888888')
#             print(stack)
#             visited.append(node) # visited 배열에 추가
#             # stack.extend(graph[node]) # 해당 노드의 자식 노드로 추가
#             stack.extend(reversed(graph[node]))

#             print('444444444')
#             print(visited)
#             print(node)
#             print(graph[node])
#             print(stack)

#     print("dfs - ", visited)
#     return visited
    
# # 함수 실행
# my_dfs(myGraph, 'G')