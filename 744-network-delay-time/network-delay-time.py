from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}

        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        queue = [k]
        i = 0

        while i < len(queue):
            node = queue[i]
            i += 1

            if node in graph:
                for nei, weight in graph[node]:
                    if dist[node] + weight < dist[nei]:
                        dist[nei] = dist[node] + weight
                        queue.append(nei)

        max_time = max(dist[1:])

        if max_time == float('inf'):
            return -1
        return max_time