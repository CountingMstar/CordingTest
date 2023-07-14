import collections


results = []

# 입력값을 그래프로 만듦
def make_graph(tickets):
    graph = collections.defaultdict(list)

    # sorted : 어휘순으로 정렬
    for a, b in sorted(tickets):
        graph[a].append(b)

    return graph


def dfs(start, graph, results):

    results.append(start)

    while graph[start]:
        # 어휘순으로 정렬되어있으므로 맨 왼쪽부터 추출
        new = graph[start].pop(0)
        dfs(new, graph, results)

    return results


tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
tickets_graph = make_graph(tickets)

answer = dfs("JFK", tickets_graph, results)
print(answer)
