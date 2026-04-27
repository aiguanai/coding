class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        hm = defaultdict(list)
        for i, (a, b) in enumerate(equations):
            hm[a].append([b,values[i]])
            hm[b].append([a,1/values[i]])
        ans = []

        def bfs(a,b):
            if a not in hm or b not in hm:
                return -1.0
            if a==b:
                return 1.0

            q = deque()
            q.append([a, 1])
            visited = set()
            while q:
                cur, val = q.popleft()
                visited.add(cur)
                for e, v in hm[cur]:
                    if e==b:
                        return val*v
                    if e not in visited:
                        q.append([e, val*v])
                        visited.add(e)
            return -1.0
                    

        return [bfs(a, b) for a, b in queries]
