#(1st attempt)
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ALL = []
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        def dfs(r, c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==-1:
                return
            for x, y in dirs:
                if not (r+x<0 or c+y<0 or r+x>=rows or c+y>=cols or grid[r+x][c+y]==-1 or grid[r+x][c+y]==0):
                    if grid[r+x][c+y]>grid[r][c]+1: #cell ka value greater than treasure se dist
                        grid[r+x][c+y]=grid[r][c]+1
                        dfs(r+x, c+y)

        for i in range(rows):
            for j in range(cols):
                if not grid[i][j]:
                    dfs(i, j)
#(post review)      
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]

        for i in range(rows):
            for j in range(cols):
                if not grid[i][j]:
                    q.append([i, j])
        
        while q:
            r, c = q.popleft()
            for x, y in dirs:
                R = r+x
                C = c+y
                if not (R<0 or C<0 or R>=rows or C>=cols or grid[R][C]==-1):
                    if grid[R][C]>grid[r][c]+1:
                        grid[R][C]=grid[r][c]+1
                        q.append([R,C])
                    
