class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        par = [i for i in range(n)]
        rank = [1] * (n)
        def find(k):
            if k!=par[k]:
                par[k] = find(par[k])
            return par[k]
        def union(a, b):
            A = find(a)
            B = find(b)
            if A==B:
                return False
            if rank[A]>rank[B]:
                rank[A]+=rank[B]
                par[B] = A
            else:
                rank[B]+=rank[A]
                par[A] = B
            return True
        
        emails = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emails:
                    union(emails[e], i)
                else:
                    emails[e]=i

        indtoemail = defaultdict(list)
        for e, i in emails.items():
            leader = find(i)
            indtoemail[leader].append(e)
        
        ans = []
        for i, e in indtoemail.items():
            ans.append([accounts[i][0]]+sorted(e))
        return ans
