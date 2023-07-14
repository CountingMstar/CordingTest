import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(times: List[List[int]], N: int, K: int) -> int:

        graph = collections.defaultdict(list)
        
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))

        # 큐 변수: [(소요 시간, 정점)]
        Q = [(0, K)]
        dist = collections.defaultdict(int)

        # 우선 순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드 최단 경로 존재 여부 판별
        if len(dist) == N:
            return max(dist.values())
        return -1


# [2, 1, 1] : [출발, 도착, 점수]
# N : 노드수
# K : 출발 노드
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2

answer = Solution.networkDelayTime(times, N, K)
print(answer)