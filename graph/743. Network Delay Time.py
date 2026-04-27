class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hm = defaultdict(list)
        for a, b, c in times:
            hm[a].append((b, c))
        dist = {i:float('inf') for i in range(1, n+1)}
        dist[k]=0
        minheap = [(0, k)]
        while minheap:
            cd, cn = heapq.heappop(minheap)
            
            if cd>dist[cn]:
                continue
            for b, c in hm[cn]:
                if c+cd<dist[b]:
                    dist[b]=c+cd
                    heapq.heappush(minheap, (c+cd, b))
        maxi = -1
        for a, v in dist.items():
            if v==float('inf'):
                return -1
            if a!=k:
                maxi = max(maxi, v)
        return maxi
