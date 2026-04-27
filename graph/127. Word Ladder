class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        hm = defaultdict(list)
        wordList.append(beginWord)
        for a in wordList:
            for i in range(len(a)):
                pattern = a[:i] + "*" + a[i+1:]
                hm[pattern].append(a)
        
        q = deque([beginWord])
        visited = set([beginWord])
        ans = 1
        while q:
            for a in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return ans
                for i in range(len(curr)):
                    pattern = curr[:i] + "*" + curr[i+1:]
                    for b in hm[pattern]:
                        if b not in visited:
                            visited.add(b)
                            q.append(b)
            ans+=1
        return 0
