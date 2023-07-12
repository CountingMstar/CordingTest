import collections


results = []


def make_graph(tickets):
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets):
        graph[a].append(b)

    return graph


def dfs(start, graph, results):

    results.append(start)

    while graph[start]:
        new = graph[start].pop(0)
        dfs(new, graph, results)

    return results


tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
tickets_graph = make_graph(tickets)

answer = dfs("JFK", tickets_graph, results)
print(answer)
