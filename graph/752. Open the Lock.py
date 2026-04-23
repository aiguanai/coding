class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        visited = set(deadends)

        q = deque()
        q.append(['0000',0])

        def nxt(txt):
            ans = []
            for i in range(4):
                ans.append(txt[:i]+str((int(txt[i])+1)%10)+txt[i+1:])
                ans.append(txt[:i]+str((int(txt[i])-1+10)%10)+txt[i+1:])
            return ans

        while q:
            txt, step = q.popleft()
            if txt==target:
                return step
            for a in nxt(txt):
                if a not in visited:
                    q.append([a,step+1])
                    visited.add(a)
        return -1
