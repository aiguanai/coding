class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        q = deque()
        rows = len(board)
        cols = len(board[0])
        for i in range(cols):
            if board[0][i]=='O':
                board[0][i]=0
                q.append([0,i])
            if board[rows-1][i]=='O':
                board[rows-1][i]=0
                q.append([rows-1,i])
        for i in range(1, rows-1):
            if board[i][0]=='O':
                board[i][0]=0
                q.append([i,0])
            if board[i][cols-1]=='O':
                board[i][cols-1]=0
                q.append([i,cols-1])
        while q:
            r, c = q.popleft()
            for x, y in dirs:
                R = r+x
                C = c+y
                val = R*cols + C+1
                if not (R<0 or C<0 or R>=rows or C>=cols or board[R][C]==0 or board[R][C]=='X'):
                    board[R][C] = 0
                    q.append([R,C])
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]==0:
                    board[i][j]='O'
        

        
