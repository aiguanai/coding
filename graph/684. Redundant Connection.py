class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1]*(n+1)

        def find(k):
            if k!=par[k]:
                par[k]=find(par[k])
            return par[k]

        def union(a,b):
            A = find(a)
            B = find(b)
            if A==B:
                return False
            if rank[A]>rank[B]:
                rank[A]+=rank[B]
                par[B]=A
            else:
                rank[B]+=rank[A]
                par[A]=B
            return True
        
        for a, b in edges:
            if not union(a,b):
                return [a,b]

            
