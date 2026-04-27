#(1st attempt)
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        grp = [-1]*n
        for i in range(n):
            for j in range(i+1):
                if isConnected[i][j]==1:
                    if grp[i]==-1 and grp[j]==-1:
                        grp[i]=i
                        grp[j]=i
                    elif grp[i]==-1:
                        grp[i]=grp[j]
                    elif grp[j]==-1:
                        grp[j]=grp[i]
                    else:
                        if grp[i]<grp[j]:
                            x = grp[j]
                            for a in range(n):
                                if grp[a]==x:
                                    grp[a]=grp[i]
                        else:
                            x = grp[i]
                            for a in range(n):
                                if grp[a]==x:
                                    grp[a]=grp[j]
        return len(set(grp))





                
        
