class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        used = []
        for i in range(n):
            used.append(False)
        
        dist = []
        for i in range(n):
            dist.append(10**9)
        
        dist[0] = 0
        result = 0
        
        for _ in range(n):
            u = -1
            
            for i in range(n):
                if used[i] == False:
                    if u == -1 or dist[i] < dist[u]:
                        u = i
            
            used[u] = True
            result += dist[u]
            
            for v in range(n):
                if used[v] == False:
                    x1 = points[u][0]
                    y1 = points[u][1]
                    x2 = points[v][0]
                    y2 = points[v][1]
                    
                    d = abs(x1 - x2) + abs(y1 - y2)
                    
                    if d < dist[v]:
                        dist[v] = d
        
        return result