class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n==0:
            return []
        if n==1:
            return [[1]]
        rep=[[0 for i in range(n)] for i in range(n)]
        row,column=0,0
        i=1
        while i<=n**2:
            while row<n and column<n and i<=n**2 and rep[row][column]==0:
                rep[row][column]=i
                i+=1
                column+=1
            row+=1
            column-=1
            while row<n and column<n and i<=n**2 and rep[row][column]==0:
                rep[row][column]=i
                i+=1
                row+=1
            column-=1
            row-=1
            while row<n and column<n and i<=n**2 and rep[row][column]==0:
                rep[row][column]=i
                i+=1
                column-=1
            column+=1
            row-=1
            while row<n and column<n and i<=n**2 and rep[row][column]==0:
                rep[row][column]=i
                i+=1
                row-=1
            column+=1
            row+=1
        return rep
