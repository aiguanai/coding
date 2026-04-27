class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]

        adj = defaultdict(list)
        size = [0]*n
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            size[a]+=1
            size[b]+=1
        
        
        leaves = deque()
        for i in range(n):
            if size[i]==1:
                leaves.append(i)

        while leaves:
            if n<=2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n-=1
                for a in adj[node]:
                    size[a]-=1
                    if size[a]==1:
                        leaves.append(a)
                



        
