import collections
from typing import List


class Solution:
    def findItinerary(tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)

        print('1111111')
        print(graph)

        route = []

        def dfs(a):
            # 첫 번째 값을 읽어 어휘순 방문
            # pop(): 젤 오른쪽에서 추출
            # pop(0): 젤 왼쪽에서 추출
            while graph[a]:
                new = graph[a].pop(0)
                print('22222222')
                print(new)
                print(graph)
                dfs(new)

            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘순 결과로
        return route[::-1]


tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
answer = Solution.findItinerary(tickets)
print(answer)