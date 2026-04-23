#(1st attempt)
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        hm = {i:set() for i in range(numCourses)} #
        for a,b in prerequisites:
            hm[b].add(a)
        ans = []
        for a,b in queries:
            visited = set()
            visited.add(b)
            q = deque()
            q.append(b)
            hlp = 0
            while q:
                curr = q.popleft()
                for i in hm[curr]:
                    if i==a:
                        ans.append(True)
                        hlp = 1
                        break
                    if i not in visited:
                        q.append(i)
                        visited.add(i)
                if hlp:
                    break
            if not hlp:
                ans.append(False)
        return ans
#(post review)

        
